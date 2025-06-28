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
        170: 5.7,
        175: 5.7,
        190: 8.3,
        195: 8.3,
        300: 8.2,
        310: 8.2,
        318: 8.1,
        319: 8.1,
        320: 8.3,
        321: 8.2,
        330: 10.9,
        380: 14.7,
        747: 14,
        20000: 5.7,
    }

    offset350 = {
        900: 12.8,
        1000: 14.8,
    }

    offset737 = {
        600: 5.7,
        700: 5.7,
        800: 5.7,
        900: 5.7,
    }

    offset777 = {
        200: 12.9,
        300: 12.8,
    }

    offset787 = {
        8: 12.6,
        9: 12.6,
        10: 12.9,
    }

    if aircraftData.idMajor == 350:
        return Distance.fromMeters(offset350.get(aircraftData.idMinor))
    elif aircraftData.idMajor == 737:
        return Distance.fromMeters(offset737.get(aircraftData.idMinor))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(offset777.get(aircraftData.idMinor))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(offset787.get(aircraftData.idMinor))
    else:
        try:
            return Distance.fromMeters(offset.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0)


@AlternativeStopPositions
def weird380(aircraftData):
    offset = {
        0: 0,
        170: 5.7,
        175: 5.7,
        190: 8.3,
        195: 8.3,
        300: 8.2,
        310: 8.2,
        318: 8.1,
        319: 8.1,
        320: 8.3,
        321: 8.2,
        330: 10.9,
        380: 12.9,
        747: 14,
        20000: 5.7,
    }

    offset350 = {
        900: 12.8,
        1000: 14.8,
    }

    offset737 = {
        600: 5.7,
        700: 5.7,
        800: 5.7,
        900: 5.7,
    }

    offset777 = {
        200: 12.9,
        300: 12.8,
    }

    offset787 = {
        8: 12.6,
        9: 12.6,
        10: 12.9,
    }

    if aircraftData.idMajor == 350:
        return Distance.fromMeters(offset350.get(aircraftData.idMinor))
    elif aircraftData.idMajor == 737:
        return Distance.fromMeters(offset737.get(aircraftData.idMinor))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(offset777.get(aircraftData.idMinor))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(offset787.get(aircraftData.idMinor))
    else:
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
        600: (eastCargo, terminalOffset),
        "600R": (CustomizedName("East Cargo Apron (600-605) | Stand 600R", 6), terminalOffset),
        "600L": (CustomizedName("East Cargo Apron (600-605) | Stand 600L", 6), terminalOffset),
        601: (eastCargo, terminalOffset),
        602: (eastCargo, terminalOffset),
        603: (eastCargo, terminalOffset),
        604: (eastCargo, terminalOffset),
        605: (eastCargo, terminalOffset),
        606: (eastService, terminalOffset),
        609: (eastService, terminalOffset),
        611: (acehub, terminalOffset),
        612: (acehub, terminalOffset),
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
        42: (terminal2Foxtrot, weird380),
        60: (terminal2Foxtrot, weird380)
    },
    GATE_G : {
        None : (terminal4Golf, terminalOffset),
    },
    GATE_H : {
        None : (changiAirbaseEast, ),
    },
    N_PARKING : {
        None : (northRemote, terminalOffset),
    },
    PARKING : {
        None : (siaHanger2, ),
    },
    0 : {
        None : (changiAirbaseWest, ),
        0 : (CustomizedName("SASCO Hanger | Stand 1", ), ),
        200 : (eastRemote, terminalOffset),
        "200L": (eastRemote, terminalOffset),
        "200R": (eastRemote, terminalOffset),
        201 : (eastRemote, terminalOffset),
        202 : (eastRemote, terminalOffset),
        "202L": (eastRemote, terminalOffset),
        "202R": (eastRemote, terminalOffset),
        203 : (eastRemote, terminalOffset),
        205 : (southEastRemote, terminalOffset),
        206 : (southEastRemote, terminalOffset),
        207 : (southEastRemote, terminalOffset),
        208 : (southEastRemote, terminalOffset),
        "208L": (southEastRemote, terminalOffset),
        "208R": (southEastRemote, terminalOffset),
        400 : (northEastRemote, terminalOffset),
        401 : (northEastRemote, terminalOffset),
        402 : (northEastRemote, terminalOffset),
        403 : (northEastRemote, terminalOffset),
        404 : (northEastRemote, terminalOffset),
    },
    W_PARKING : {
        None : (westCargo, terminalOffset),
        "516L": (CustomizedName("West Cargo Apron (502-517) | Stand 516L", 5), terminalOffset),
        "516R": (CustomizedName("West Cargo Apron (502-517) | Stand 516R", 5), terminalOffset),
        "517L": (CustomizedName("West Cargo Apron (502-517) | Stand 517L", 5), terminalOffset),
        "517R": (CustomizedName("West Cargo Apron (502-517) | Stand 517R", 5), terminalOffset),
    },
}
