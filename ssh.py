import base64
import paramiko
key = paramiko.RSAKey(data=base64.b64decode(b'AAAAB3NzaC1yc2EAAAADAQABAAABAQC4Yk1Ql79ji1NEMTOJ212idd8u61g07JS0vbdHYKo7NV6bEgSvLKfw5RfCmpXk5xtked2Tu6nLKP1P5eU8OXstaSpV7kthMOP2uIcfm741CrQQkP+ojdlYPVsEpwnXrFyclBqgHzl7SifWZwioElXXeZE2r1csEG3HKtDcVVWvPwFGG9NfecUsPeLB6sHwyWdChCWfD1KVa0GGU3kBbWRb1d87nj/JdK+qrCgIggMk+To6cJBeS6k4K+bNnRikJgH1btS49RS73tdfUB72HbukPfXhzcRqj9gTSoRs+h37FkwGDB5CPwslFpDhYdj9RGjZa1i7cjlKRL2LiJr/LCX/ rahmed@Razis-MBP.fios-router.home'))
client = paramiko.SSHClient()
client.get_host_keys().add('10.0.0.2', 'ssh-rsa', key)
client.connect('appolo', username='rahmed', password='asdf')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()