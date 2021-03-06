import pickle

__all__ = ["get_conjectures"]


def get_conjectures(target):
    """Returns current stored conjectures on graph invariant target.
    Parameters
    ----------
    target :   string
               A graph invariant computable by grinpy.

    Returns
    -------
    db :   dictionary
           The dictionary with key values equal to conjectured inequalities
           and whose values are associated with a given conjecture.
    """
    with open(f"TxGraffiti/conjectures/{target}_conjectures", "rb") as pickle_file:
        db = pickle.load(pickle_file)
    return db
