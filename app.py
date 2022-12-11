import faiss
import pickle
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

from dotenv import load_dotenv
import os
import requests
from rich import print
from googletrans import Translator

#engine = create_engine('postgresql://rairo@pubag:pubag1036!@pubag.postgres.database.azure.com:5432/postgres')


#conn = engine.connect()

translator = Translator()



def vector_search(query, model, index, num_results=10):
    """Tranforms query to vector using a pretrained, sentence-level
    DistilBERT model and finds similar vectors using FAISS.
    Args:
        query (str): User query that should be more than a sentence long.
        model (sentence_transformers.SentenceTransformer.SentenceTransformer)
        index (`numpy.ndarray`): FAISS index that needs to be deserialized.
        num_results (int): Number of results to return.
    Returns:
        D (:obj:`numpy.array` of `float`): Distance between results and query.
        I (:obj:`numpy.array` of `int`): Paper ID of the results.

    """
    vector = model.encode(list(query))
    D, I = index.search(np.array(vector).astype("float32"), k=num_results)
    return D, I


def id2details(df, I, column):
    """Returns the paper titles based on the paper index."""
    return [list(df[df.id == idx][column]) for idx in I[0]]


@st.cache
def read_data(data="agri_pub2.csv"):
    """Read the data from local."""
    return pd.read_csv(data)


@st.cache(allow_output_mutation=True)
def load_bert_model(name="distilbert-base-nli-stsb-mean-tokens"):
    """Instantiate a sentence-level DistilBERT model."""
    return SentenceTransformer(name)


@st.cache(allow_output_mutation=True)
def load_faiss_index(path_to_faiss="faiss_index.pickle"):
    """Load and deserialize the Faiss index."""
    with open(path_to_faiss, "rb") as h:
        data = pickle.load(h)
    return faiss.deserialize_index(data)


def detect_language(text):
    language = translator.detect(text)
    language_text = language.lang
    # Return the language
    return language_text


def translate(text, src, dest):

    # Get translation
    translation = translator.translate(text,src,dest)
    translation_text = translation.text
    # Return the translation
    return translation_text



def main():

    try:
        # Get Configuration Settings


        text = 'hello!'
        print(text)
        print('Detected language of "' + text + '":',
              detect_language(text))
        print("Type:", type(detect_language(text)))
        dest = 'es'
        print(dest + ":", translate(text, 'en',
              dest))
    except Exception as ex:
        print("exception:", ex)

    # Load data and models
    data = read_data()
    model = load_bert_model()
    faiss_index = load_faiss_index()

    st.title("Agro Science Search Powered by PubAG")

    # User search
    user_input = st.text_area(
        "Search", "")

    # Filters
    st.sidebar.markdown("**Filters**")
    filter_year = st.sidebar.slider(
        "Publication year", 1914, 2021, (1914, 2021), 1)
    num_results = st.sidebar.slider("Number of search results", 3, 10, 3)

    # Fetch results
    if user_input:
        # Get paper IDs

        sc = detect_language(text)
        st.write(sc)
        user_input = translate(user_input, sc,'en')
        D, I = vector_search([user_input], model, faiss_index, num_results)
        # Slice data on year
        frame = data[
            (data.publication_year >= filter_year[0])
            & (data.publication_year <= filter_year[1])
        ]
        #st.write(I)
        # Get individual results
        results = []
        for id_ in I.flatten().tolist():
            if id_ in set(frame.id):
                f = frame[(frame.id == id_)]
                a = (user_input, f.iloc[0].title)
                results.append(a)
                print(results)
            else:
                continue

            st.subheader(
                translate(f.iloc[0].title, 'en',
                          sc))
            st.write(f.iloc[0].url)
            st.write(f.iloc[0].publication_year)

            st.markdown(translate(f.iloc[0].abstract, 'en',
                                  sc))


if __name__ == "__main__":
    main()
