from abc import ABC, abstractmethod
import random

class Plan(ABC):

    def get_excerpt(self):
        return 'excerpt from the article'

    def get_article(self):
        return 'full article'

    def get_ads(self):
        return 'some ads'

    @abstractmethod
    def get_call_to_action(self):
        pass

# Concrete Implementation 1
class PlanA(Plan):

    def get_call_to_action(self):
        return 'Pay 10 $ a month to remove ads'

# Concrete Implementation 2
class PlanB(Plan):

    def get_call_to_action(self):
        return 'Remove ads with just 10 $ a month'
# Abstract Interface (aka Handle) used by the client
class Website(ABC):

    def __init__(self, plan):
        # encapsulate an instance of a concrete implementation class
        self._plan = plan

    def __str__(self):
        return 'Interface: {}; Plan: {}'.format(
            self.__class__.__name__, self._plan.__class__.__name__)

    @abstractmethod
    def show_page(self):
        pass

# Concrete Interface 1
class FreeWebsite(Website):

    def show_page(self):
        ads = self._plan.get_ads()
        text = self._plan.get_excerpt()
        call_to_action = self._plan.get_call_to_action()
        print(ads)
        print(text)
        print(call_to_action)
        print('')

# Concrete Interface 2
class PaidWebsite(Website):

    def show_page(self):
        text = self._plan.get_article()
        print(text)
        print('')

# Client
def main():
    a_free = FreeWebsite(PlanA())
    print(a_free)
    a_free.show_page()  # the client interacts only with the interface

    b_free = FreeWebsite(PlanB())
    print(b_free)
    b_free.show_page()

    a_paid = PaidWebsite(PlanA())
    print(a_paid)
    a_paid.show_page()

    b_paid = PaidWebsite(PlanB())
    print(b_paid)
    b_paid.show_page()

if __name__ == '__main__':
    main()


