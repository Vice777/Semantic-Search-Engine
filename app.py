import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

ELASTIC_CLOUD_ID = st.secrets["ELASTIC_CLOUD_ID"]
ELASTIC_API_KEY = st.secrets["ELASTIC_API_KEY"]

client = Elasticsearch(
    cloud_id=ELASTIC_CLOUD_ID,
    api_key=ELASTIC_API_KEY,
    verify_certs=True,
    request_timeout=60
)

# Load SentenceTransformer model (you can cache it using joblib or Hugging Face API)
model = SentenceTransformer('all-distilroberta-v1')

# Function to format and print search results
def pretty_response(response):
    # print("Executing pretty response \n\n")
    if len(response['hits']['hits']) == 0:
        print('Your search returned no results.')
    else:
        for hit in response['hits']['hits']:
            id_ = hit['_source']['id']
            score = hit['_score']
            name = hit['_source']['name']
            decision_date = hit['_source']['decision_date']
            head_matter = hit["_source"]["head_matter"]

            pretty_output = (
                f"  \n  ID: {id_}  \n  Name: {name}  \n  Decision Date: {decision_date}  \n  Head Matter: {head_matter}  \n  Score: {score}"
            )
            st.write(pretty_output)

# Function to perform semantic search
def semantic_search(query, k_query):
    response = client.options(request_timeout=60).search(
        index="legal_index_1",
        knn={
            "field": "text_vector",
            "query_vector": model.encode(query),
            "k": k_query,
            "num_candidates": 100
        }
    )
    return response


# Home Page
def home_page():
    st.title("Legal Cases Semantic Search App")
    st.write("Welcome to our app! This app allows you to perform semantic search on legal cases.")
    st.write("Navigate to the 'Input' page to perform a semantic search.")

# Input Page
def input_page():
    st.title("Input")
    st.write("Please enter your query and the number of results you would like to see.")
    
    if st.button("Use Default Sample Query"):
        default_query = (
            "Clark, C. J.\nTbe plaintiff executed to defendant Burusell two notes for $400 eacb, payable at tbe National Bank of New Bern, respectively,- on 3 January, 1914, and 3 September, 1914, for tbe balance due on purchase of a “merry-go-round” on wbicb be bad made a casb payment. ..."  # Paste the default query text here
        )
        st.session_state.query_text = default_query  # Set the default query text

    # Input text for legal cases
    query_text = st.text_area("Enter text related to legal cases", value=st.session_state.get("query_text", ""))

    # Parameter for number of closest documents
    num_closest_docs = st.slider("Number of closest documents", min_value=1, max_value=20, value=5)

    if st.button("Perform Semantic Search"):
        search_results = semantic_search(query_text, num_closest_docs)

        # Display search results
        if search_results:
            st.write("Search Results:")
            # Display search results in a DataFrame or formatted manner
            # Modify the display according to your search result format
            response = pretty_response(search_results)
            st.write(response)
        else:
            st.write("No results found.")


# Streamlit app
def main():
    page = st.sidebar.selectbox("Select a page", ["Home", "Input"])
    
    if page == "Home":
        home_page()
    elif page == "Input":
        input_page()

if __name__ == "__main__":
    main()