import os
import voyageai
from supabase import create_client, Client
from dotenv import load_dotenv
from utils.config_ import lib_config

load_dotenv()

VOYAGE_API_KEY = os.getenv("VOYAGE_AI_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

vo = voyageai.Client(api_key=VOYAGE_API_KEY)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_embedding_results(
    user_query: str,
    match_count
) -> list[dict]:
    
    """
    Takes a user query and then:

    (1) - converts to vector of len 1024 via embedding model
    (2) - sends embedding to rpc function hosted on Supabase
    (3) - rpc function computes cosine similarity and returns nearest matches

    returns:
    list of objects from database 
    """

    # (1) embed user query
    response_vo = vo.embed(
        user_query,
        model = lib_config.EMBEDDING_MODEL,
        input_type = "query",
        output_dimension= lib_config.EMBEDDING_OUT_DIMS
    )

    embedding = response_vo.embeddings[0]

    # (2) (3) send embedding to inner product function hosted on supabase

    response_sb = (
        supabase.rpc(
            "match_rag_demo", {
                "query_embedding": embedding, 
                "match_threshold": lib_config.DISTANCE_MATCH_THRESHOLD, 
                "match_count": match_count
            }
        ).execute()
    )

    return response_sb.data
