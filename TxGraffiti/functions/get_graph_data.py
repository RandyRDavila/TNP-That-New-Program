import pickle

__all__ = ["get_graph_data", "get_hypothesis_data"]


def get_graph_data(family):
    """
    Parameters
    ----------

    family :   string
               A name of a given graph family stored in TxGraffiti.

    Returns
    -------
    db :   dictionary
           
    """
    with open(f"TxGraffiti/graph_data/{family}_db", "rb") \
        as pickle_file:
        db = pickle.load(pickle_file)
    return db

def get_hypothesis_data():
    """
    
    Returns
    -------
    list : A list of possible combinations of hypothesis
    """
    with open(f"TxGraffiti/graph_data/hypothesis_db", "rb") \
        as pickle_file:
        db = pickle.load(pickle_file)
    return db