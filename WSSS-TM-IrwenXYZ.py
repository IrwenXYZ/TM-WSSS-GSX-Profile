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
eastRemote = CustomizedName("East Remote Apron (200-203) | Stand #§", 10)
southEastRemote = CustomizedName("South East Remote Apron (205-208) | Stand #§", 11)
northRemote = CustomizedName("North Remote Apron (300-310, 951-954) | Stand #§", 12)
northEastRemote = CustomizedName("North East Remote Apron (400-404) | Stand #", 13)
southApron = CustomizedName("South Apron (461-487) | Stand #", 14)
westCargo = CustomizedName("West Cargo Apron (502-517) | Stand #", 5)
eastCargo = CustomizedName("East Cargo Apron (600-605) | Stand #", 6)
eastService = CustomizedName("East Service Apron (606, 609) | Stand #", 7)
acehub = CustomizedName("Acehub (611-612) | Stand #", 9)
siaHanger2 = CustomizedName("SIA Hanger 2 | Stand #", 15)
changiAirbaseEast = CustomizedName("Changi Airbase East | Stand #", 16)
changiAirbaseWest = CustomizedName("Changi Airbase West | Stand #", 17)

@AlternativeStopPositions
def terminalOffset(aircraftData):
    offset = {
        0: 0,
        310: 8.2,
        320: 8.3,
        380: 14.7,
        747: 14,
    }

    try:
        return Distance.fromMeters(offset.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)

parkings = {
    E_PARKING : {
        None: (southApron, ),
        "462L": (CustomizedName("South Apron (461-487) | Stand 462L", 14), ),
        "462R": (CustomizedName("South Apron (461-487) | Stand 462R", 14), ),
        "463L": (CustomizedName("South Apron (461-487) | Stand 463L", 14), ),
        "463R": (CustomizedName("South Apron (461-487) | Stand 463R", 14), ),
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
        None : (terminal3Alpha, terminalOffset),
    },
    GATE_B : {
        None : (terminal3Bravo, terminalOffset),
    },
    GATE_C : {
        None : (terminal1Charlie, terminalOffset),
    },
    GATE_D : {
        None : (terminal1Delta, terminalOffset),
    },
    GATE_E : {
        None : (terminal2Echo, terminalOffset),
    },
    GATE_F : {
        None : (terminal2Foxtrot, terminalOffset),
    },
    GATE_G : {
        None : (terminal4Golf, terminalOffset),
    },
    GATE_H : {
        None : (changiAirbaseEast, ),
    },
    N_PARKING : {
        None : (northRemote, ),
    },
    PARKING : {
        None : (siaHanger2, ),
    },
    0 : {
        None : (changiAirbaseWest, ),
        0 : (CustomizedName("SASCO Hanger | Stand 1", ), ),
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
        None : (westCargo, terminalOffset),
        "516L": (CustomizedName("West Cargo Apron (502-517) | Stand 516L", 5), terminalOffset),
        "516R": (CustomizedName("West Cargo Apron (502-517) | Stand 516R", 5), terminalOffset),
        "517L": (CustomizedName("West Cargo Apron (502-517) | Stand 517L", 5), terminalOffset),
        "517R": (CustomizedName("West Cargo Apron (502-517) | Stand 517R", 5), terminalOffset),
    },
}
