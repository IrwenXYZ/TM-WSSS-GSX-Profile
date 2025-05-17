# -- coding: utf-8 --
msfs_mode = 1
icao = "wsss"

terminal3Alpha = CustomizedName("Terminal 3 A Gates | Gate A#§", 3)
terminal3Bravo = CustomizedName("Terminal 3 B Gates | Gate B#§", 3)
terminal1Charlie = CustomizedName("Terminal 1 C Gates | Gate C#§", 1)
terminal1Delta = CustomizedName("Terminal 1 D Gates | Gate D#§", 1)
terminal2Echo = CustomizedName("Terminal 2 E Gates | Gate E#§", 2)
terminal2Foxtrot = CustomizedName("Terminal 2 F Gates | Gate F#§", 2)
terminal4Golf = CustomizedName("Terminal 4 G Gates | Gate G#§", 4)
eastRemote = CustomizedName("East Remote Apron (200-203) | Stand #§", 7)
southEastRemote = CustomizedName("South East Remote Apron (205-208) | Stand #§", 8)
northRemote = CustomizedName("North Remote Apron (300-310, 951-954) | Stand #§", 9)
northEastRemote = CustomizedName("North East Remote Apron (400-404) | Stand #", 10)
southApron = CustomizedName("South Apron (461-487) | Stand #", 11)
westCargo = CustomizedName("West Cargo Apron (502-517) | Stand #", 5)
eastCargo = CustomizedName("East Cargo Apron (600-605) | Stand #", 6)
eastService = CustomizedName("East Service Apron (606, 609) | Stand #", 12)
acehub = CustomizedName("Acehub (611-612) | Stand #", 13)
siaHanger2 = CustomizedName("SIA Hanger 2 | Stand #", 14)

parkings = {
    E_PARKING : {
        None: (southApron, ),
        "462L": (CustomizedName("South Apron (461-487) | Stand 462L", 11), ),
        "462R": (CustomizedName("South Apron (461-487) | Stand 462R", 11), ),
        "463L": (CustomizedName("South Apron (461-487) | Stand 463L", 11), ),
        "463R": (CustomizedName("South Apron (461-487) | Stand 463R", 11), ),
        600: (eastCargo, ),
        "600R": (CustomizedName("East Cargo Apron (600-605) | Stand 600R", 6), ),
        "600L": (CustomizedName("East Cargo Apron (600-605) | Stand 600L", 6), ),
        601: (eastCargo, ),
        602: (eastCargo, ),
        603: (eastCargo, ),
        604: (eastCargo, ),
        605: (eastCargo, ),
        606: (eastService, ),
        609: (eastService, ),
        611: (acehub, ),
        612: (acehub, ),
    },
    GATE_A : {
        None : (terminal3Alpha, )
    },
    GATE_B : {
        None : (terminal3Bravo, )
    },
    GATE_C : {
        None : (terminal1Charlie, )
    },
    GATE_D : {
        None : (terminal1Delta, )
    },
    GATE_E : {
        None : (terminal2Echo, )
    },
    GATE_F : {
        None : (terminal2Foxtrot, )
    },
    GATE_G : {
        None : (terminal4Golf, )
    },
    N_PARKING : {
        None : (northRemote, ),
    },
    PARKING : {
        None : (siaHanger2, ),
    },
    0 : {
        None : (CustomizedName("Extra Gate #", ), ),
        0 : (CustomizedName("SASCO Hanger", ), ),
        200 : (eastRemote, ),
        "200L": (eastRemote, ),
        "200R": (eastRemote, ),
        201 : (eastRemote, ),
        202 : (eastRemote, ),
        "202L": (eastRemote, ),
        "202R": (eastRemote, ),
        203 : (eastRemote, ),
        205 : (southEastRemote, ),
        206 : (southEastRemote, ),
        207 : (southEastRemote, ),
        208 : (southEastRemote, ),
        "208L": (southEastRemote, ),
        "208R": (southEastRemote, ),
        400 : (northEastRemote, ),
        401 : (northEastRemote, ),
        402 : (northEastRemote, ),
        403 : (northEastRemote, ),
        404 : (northEastRemote, ),
    },
    W_PARKING : {
        None : (westCargo, ),
        "516L": (CustomizedName("West Cargo Apron (502-517) | Stand 516L", 5), ),
        "516R": (CustomizedName("West Cargo Apron (502-517) | Stand 516R", 5), ),
        "517L": (CustomizedName("West Cargo Apron (502-517) | Stand 517L", 5), ),
        "517R": (CustomizedName("West Cargo Apron (502-517) | Stand 517R", 5), ),
    },
}
