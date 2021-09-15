0.11.0 (15-09-2021)
-------------------
- Drop python 2 support
- crabpy updaten (#148)


0.10.0 (13-08-2021)
-------------------
- "naam" toevoegen aan straat renderer (#145)

0.9.0 (08-04-2021)
------------------

- Drop suppport for Python 3.4 and 3.5. Supported versions are 2.7, 3.6, 3.7 and 3.8. This is the last version to support Python 2.
- Updated to the latest pyCountry versions and adapted the API. (#119, #135)
- Added the shape file of a perceel to the renderer. (#122)
- Remove pyup integration (#133)
- GetPostkantonByHuisnummerId ontsluiten (#138)
- Sort parameter toevoegen aan alle requests (#140)

0.8.1 (06-06-2019)
------------------

- Etag tween geeft soms errors (#102)

0.8.0 (11-01-2019)
------------------

- Caching tween volledig herwerken (#97)

0.7.0 (2019-01-03)
------------------

- Update crabpy to get new deelgemeente codes (#84, #92)
- Include CAPAKEY by default (#46)
- Allow passing custom crab wsdl (#75)

0.6.3 (2017-12-07)
------------------

- Make compatbile with CRABpy 0.8.3
- Make compatible with latest pyCountry. (#56)

0.6.2 (2017-08-29)
------------------

- Make compatible with CRABpy 0.8.2

0.6.1 (2017-04-20)
------------------

- Make compatible with CRABpy 0.8.1 and fix center and bounding box formats in responses (#47)

0.6.0 (2017-04-19)
------------------

- Make compatible with CRABpy 0.8.0 and use the CAPAKEY REST gateway (#40)
- Blacklist for conditional tween (#41)

0.5.1 (2016-11-22)
------------------

- Add niscode to CRAB gemeente renderer. (#39)

0.5.0 (2016-07-27)
------------------

- Add HTTP caching headers. Both conditional GET with ETags and Cache-Control
  headers. Caching times are based on the ones passed to the gateways. (#37)
- Empty proxy settings are filtered out before being passed to the gateways. (#38)

0.4.1 (2016-02-02)
------------------

- Better error handling for capakey views. Generate HTTP 404 Not Found instead
  of HTTP 500 Internal Server Error. (#36)

0.4.0 (2016-01-25)
------------------

- Update dependencies. Update pycountry to version 1.19.
- Add explicit support for python 3.5.
- Add deelgemeenten. (#33)
- Added postadressen in a few places.
- Added a list of huisnummers to a CRAB perceel.

0.3.0 (2015-06-01)
------------------

- Add Adresposities. Add endpoints that exposes the Adresposities linked to a
  certain Huisnummer or Subadres. (#26) [TalissaJoly]
- Add Landen (countries). Add endpoints to get a list of Landen or more 
  information about a single Land. (#30, #31) [TalissaJoly]
- Return HTTP 404 errors for certain unexisting resources. (#25) [TalissaJoly]
- Limit the number of results that can be returned in a list. There was some
  partial handling for this, but only when the user did not send any range
  headers. This behavious was deemed potentially hazardous and changed. Now,
  only a maximum of 5.000 records will be returned and range slicing works
  correctly. (#16) [TalissaJoly]

0.2.0 (2015-03-03)
------------------

- Implement two service endpoints dealing with Subadressen (think of boxes
  in an appartment building). (#18) [TalissaJoly]
- Implement a service endpoint for listing the Postkantons (ie. Postcode) in
  a certain gemeente. (#23) [TalissaJoly]
- Cleanedthe code a bit by removing unneeded bits and pieces. (#17) (#19)
  [TalissaJoly]

0.1.1 (2014-09-18)
------------------

- Minor release adding and cleaning up lots of service documentation. (#14)
- Fixes a small bug when no capakey username or password was set and the capakey
  service was included. 

0.1.0 (2014-09-05)
------------------

- First stable release, matches with CRABpy 0.4.1
- Exposes CRAB and CAPAKEY gateways.
- CRAB Gateway also exposes some Provincie objects. (#13)
- CRAB and CAPAKEy can be configured independently. (#11)

0.1.0a2 (2014-04-30)
--------------------

- Still alpha.
- Coveralls support.
- Proxy settings in ini file. (#5)
- Range headers. (#9)

0.1.0a1 (2014-03-19)
--------------------

- Initial version
