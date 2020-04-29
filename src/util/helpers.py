def filter_comments(comment, kwargs):
    """Basic filter condition to be used in list comprehension

    :param comment: Comment
    :type comment: dict
    :param kwargs: Conditions to be evaluated agains `comment`
    :type kwargs: dict
    :return: Whether `comment` satisfies the conditions in `kwargs`
    :rtype: bool
    """
    for kw in kwargs:
        if kw in comment:
            if isinstance(kwargs[kw], str) and kwargs[kw] not in comment[kw]:
                return False
            elif isinstance(kwargs[kw], int) and kwargs[kw] != comment[kw]:
                return False

    return True
