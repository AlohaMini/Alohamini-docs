# FAQ

[Return to official manual](../official-manual.md)

Before updating the software, please save the local configuration and uncommitted changes. The network proxy address should be replaced with your own server address.

(yq-cyrmk57grrm79vgo-u2517d6ae)=

Update lerobot_alohamini in Raspberry Pi to the latest version:
1. Check and save local changes

(yq-cyrmk57grrm79vgo-uea5587d9)=

`git status`: Check the differences first and save your configuration and calibration-related changes; if there are unprocessed changes, complete the backup or submit first.

(yq-cyrmk57grrm79vgo-u0be853b4)=

2. Pull the code

(yq-cyrmk57grrm79vgo-ud8441ecf)=

git pull --ff-only

(yq-cyrmk57grrm79vgo-u965c1d76)=

3. Already up to date will be displayed when there are no new submissions; changes will be listed when there are updates. When conflicts occur or fast forwarding is not possible, branch differences are handled first.

(yq-cyrmk57grrm79vgo-u977d1848)=

(yq-cyrmk57grrm79vgo-u762fd25a)=

If github cannot be accessed, set the crash to allow intranet access, and then execute on the Raspberry Pi:
export http_proxy=[http://192.168.50.XXX:7890](http://192.168.50.XXX:7890)

(yq-cyrmk57grrm79vgo-u06cd1583)=

export https_proxy=[http://192.168.50.XXX:7890](http://192.168.50.XXX:7890)

(yq-cyrmk57grrm79vgo-ucc3369d5)=

(yq-cyrmk57grrm79vgo-u6c47f826)=

Test:

(yq-cyrmk57grrm79vgo-uc581c3a6)=

curl [https://github.com](https://github.com)

(yq-cyrmk57grrm79vgo-u58b10dde)=

curl https://google.com

(yq-cyrmk57grrm79vgo-u1653f7e3)=

(yq-cyrmk57grrm79vgo-u5f045e91)=

This shows that the Raspberry Pi can access the external network normally, and git pull --ff-only will no longer report an error.
