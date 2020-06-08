import tensorflow as tf
import tensorlayer as tl
import numpy as np
from tensorlayer.cost import cross_entropy_seq, cross_entropy_seq_with_mask
from tqdm import tqdm
from sklearn.utils import shuffle
from data.twitter import data
from tensorlayer.models.seq2seq import Seq2seq
from tensorlayer.models.seq2seq_with_attention import Seq2seqLuongAttention
import os
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium import webdriver
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def initial_setup(data_corpus):
    metadata, idx_q, idx_a = data.load_data(PATH='data/{}/'.format(data_corpus))
    (trainX, trainY), (testX, testY), (validX, validY) = data.split_dataset(idx_q, idx_a)
    trainX = tl.prepro.remove_pad_sequences(trainX.tolist())
    trainY = tl.prepro.remove_pad_sequences(trainY.tolist())
    testX = tl.prepro.remove_pad_sequences(testX.tolist())
    testY = tl.prepro.remove_pad_sequences(testY.tolist())
    validX = tl.prepro.remove_pad_sequences(validX.tolist())
    validY = tl.prepro.remove_pad_sequences(validY.tolist())
    return metadata, trainX, trainY, testX, testY, validX, validY


def inference(seed, top_n):
    model_.eval()
    seed_id = [word2idx.get(w, unk_id) for w in seed.split(" ")]
    sentence_id = model_(inputs=[[seed_id]], seq_length=20, start_token=start_id, top_n = top_n)
    sentence = []
    for w_id in sentence_id[0]:
        w = idx2word[w_id]
        if w == 'end_id':
            break
        sentence = sentence + [w]
    return sentence
def testdata(seed):
    data_corpus = "chatapp"

    #data preprocessing
    metadata, trainX, trainY, testX, testY, validX, validY = initial_setup(data_corpus)

    # Parameters
    src_len = len(trainX)
    tgt_len = len(trainY)

    assert src_len == tgt_len

    batch_size = 32
    n_step = src_len // batch_size
    src_vocab_size = len(metadata['idx2w']) # 8002 (0~8001)
    emb_dim = 1024

    word2idx = metadata['w2idx']   # dict  word 2 index
    idx2word = metadata['idx2w']   # list index 2 word

    unk_id = word2idx['unk']   # 1
    pad_id = word2idx['_']     # 0

    start_id = src_vocab_size  # 8002
    end_id = src_vocab_size + 1  # 8003

    word2idx.update({'start_id': start_id})
    word2idx.update({'end_id': end_id})
    idx2word = idx2word + ['start_id', 'end_id']

    src_vocab_size = tgt_vocab_size = src_vocab_size + 2

    num_epochs = 100
    vocabulary_size = src_vocab_size
    def inference(seed, top_n):
        model_.eval()
        seed_id = [word2idx.get(w, unk_id) for w in seed.split(" ")]
        sentence_id = model_(inputs=[[seed_id]], seq_length=20, start_token=start_id, top_n = top_n)
        sentence = []
        for w_id in sentence_id[0]:
            w = idx2word[w_id]
            if w == 'end_id':
                break
            sentence = sentence + [w]
        return sentence

    decoder_seq_length = 20
    model_ = Seq2seq(
        decoder_seq_length = decoder_seq_length,
        cell_enc=tf.keras.layers.GRUCell,
        cell_dec=tf.keras.layers.GRUCell,
        n_layer=3,
        n_units=256,
        embedding_layer=tl.layers.Embedding(vocabulary_size=vocabulary_size, embedding_size=emb_dim),
        )

    load_weights = tl.files.load_npz(name='model.npz')
    tl.files.assign_weights(load_weights, model_)
       
    top_val=''
    leng=400
    top_n = 3
    for i in range(top_n):
        sentence = inference(seed, top_n)
        value=str(' '.join(sentence)).replace("unk","")
        if len(value)<leng:
            top_val=value
            leng=len(value)
    top_val=top_val.strip()
    prev=top_val
    return top_val



driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://web.whatsapp.com/")

#only DMs and no group messages by checking mute icon.

friends_lists = ['Me']


wait = WebDriverWait(driver, 600)

input("Press anything after QR scan")
prev=""
while True:
    for friend in friends_lists:
        time.sleep(10)
        persons = driver.find_elements_by_class_name('_2wP_Y')
        print(len(persons))
        for person in persons:
            try:
                if person.text not in ['CHATS','MESSAGES']:
                    person_title = person.find_element_by_class_name('_1wjpf')
                   # print(person_title.get_attribute("title"))
                    user=str(person_title.get_attribute("title"))
                    if user=='Username':
                        person_contact = person.find_element_by_class_name('_2EXPL')
                        person_contact.click()
                        person_msg = person.find_element_by_class_name('_2_LEW')
                        message=str(person_msg.get_attribute("title"))
                        message = ''.join(filter(lambda c: c in string.printable, message))
                        prev = ''.join(filter(lambda c: c in string.printable, prev))
                        print("#"+message+"#"+prev+"#")
                        if message!=prev:
                            reply_msg=testdata(message)
                            message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
                            message.send_keys(reply_msg)

                            sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                            sendbutton.click()
                            prev=str(reply_msg)
            except:
                print("*")
                continue
