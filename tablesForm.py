class Table1:
    """
    This represents the Table1 entity.
    It has a relationship with Table2 and Pool entities.
    """
    pass

class Table2:
    """
    This represents the Table2 entity.
    It has a relationship with Table1 entity.
    """
    pass

class Pool:
    """
    This represents the Pool entity which is not a table.
    It has a relationship with Table1.
    """
    pass
