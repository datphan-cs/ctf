import owiener
from binascii import unhexlify
e = 11166103196154889752303220892239651795733546278404023938241695257049616486269510849614478851777032952295215682883137553875612698329733445279067836281213983994407488309007532454112030920083980715039165478010594913811396567217622912540882936697549439279978846838816609657401069595009396064191814785568231226437

n =  73637296244952424176022809874182764338824165860557441248256355894263681529325132358243986527875426906713043834572242199738974812553087183123585680396295748170383846431534870974268411308126910669340816312739282239127020399658360987453076390908852868364930604260096085804637379678701061503606538746552186621781

enc = 33388797154298850359361288692345250057731783296146664027216804177694545471283312186238743373320480657232678314840778793310567758027794467059546151784948963867910200215642593662956692866861274294096964186852973971009394731124712842365652330253150898245422665887395687336792910348483419537993408785837494736860

d = owiener.attack(e,n)

dec = pow(enc,d,n)
print(unhexlify(hex(dec)[2:]).decode())