# encoding:utf-8


class Base(object):

    def from_dict(self, obj):
        """
        :return:
        """
        pass

    def dict(self):
        """
        :return:
        """
        return {key: value for key, value in self.__dict__.items()}

    def __repr__(self):
        """
        :return:
        """
        items = ["%s:%s" % (item, value) for item, value in self.__dict__.items()]
        return "%s<%s>" % (self.__class__.__name__, ",".join(items))
