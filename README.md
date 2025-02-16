# maldomaindata_convert

Convert a comma separated list of domain reputation data to a list of domains that can be imported by pi-hole (https://pi-hole.net/)

## Sample Data Import Format:

domain, category, score, first_seen, last_seen, ports (|)

      bad.tld,27,85,2022-01-25,2022-01-26,80
      test.xyz,27,123,2022-01-25,2022-01-26,80 443
      malware.org,27,104,2022-01-25,2022-01-26,443

## Sample Data Export Format:

      bad.tld
      test.xyz
      malware.org

## Authors
[Jason Ford](http://www.jasonsford.com)

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
