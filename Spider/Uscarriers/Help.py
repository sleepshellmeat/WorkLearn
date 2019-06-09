a = """
Keel Laid: August 15, 1970
          Christened: October 11, 1975
          Commissioned: October 18, 1977

          Builder: Newport News Shipbuilding Co., Newport News, Va.
          Propulsion system: two Westinghouse A4W nuclear reactors,
           four steam turbines, four shafts,  260,000 shp (194 MW)
          Lengths, overall: 1.092 feet (332.85 meters)
          Flight Deck Width: 252 feet (76.8 meters)
          Area of flight deck: about 4.5 acres (18211.5 m2)
          Beam: 134 feet (40.84 meters)
          Draft: 37.7 feet (11.3 meters)
          Displacement: approx. 101,000-104,000 tons full load
          Speed: 30+ knots
          Planes: 90 fixed wing and helicopters
          Crew: Ship: 3,200 ; Air Wing: 2,480
          Armament:
           - two Rolling Airframe Missile (RAM) launchers
           - four MK-38 Mod 2 25mm Machine Gun Systems (MGS)
           - two MK-29 Mod 3 NATO Sea Sparrow launchers
           - two MK-15 20mm Phalanx CIWS
          Homeport: Norfolk, VA.
"""
lt = a.split('\n')
ltt = ' '.join(lt).strip().split('           ')
# print(ltt)
t = 4
while 1 < t:
    for i in range(len(ltt)):
        if ltt[i].find(':') == -1 or ltt[i].find('-') != -1:
            a = ltt[i-1] + ltt[i]
            t -= 1
            print(a)

