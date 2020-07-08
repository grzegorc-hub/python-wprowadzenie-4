print('mod init')
z = 3

from . import spam                # Import względny w stosunku do pakietu (szuka spam tylko w tym katlogu co jestem)
from .spam import name
print(spam.name)
print(name)