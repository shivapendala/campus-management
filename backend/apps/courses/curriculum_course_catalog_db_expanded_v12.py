"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 14

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for EEE and ECE courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V12: Dict[str, Dict[str, Any]] = {
    "EE701": {
        "code": "EE701",
        "title": "High Voltage Engineering",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electrical & Electronics Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Conduction & Breakdown in Gases",
                "topics": [
                    "Gases as insulating media, collision processes, ionization processes.",
                    "Townsend's criterion for breakdown, Townsend's primary and secondary ionization coefficients.",
                    "Streamer theory of breakdown in gases, Paschen's law and its limitations.",
                    "Breakdown in non-uniform fields and corona discharges, post-breakdown phenomenon."
                ]
            },
            {
                "unit": 2,
                "title": "Conduction & Breakdown in Liquids & Solids",
                "topics": [
                    "Liquid dielectrics: Pure and commercial liquids, conduction and breakdown in pure liquids.",
                    "Breakdown mechanisms in commercial liquids: suspended particle, cavity, and electroconvection mechanisms.",
                    "Solid dielectrics: Intrinsic breakdown, electromechanical breakdown, thermal breakdown.",
                    "Chemical and electrochemical deterioration, treeing and tracking, partial discharges."
                ]
            },
            {
                "unit": 3,
                "title": "Generation of High Voltages & Currents",
                "topics": [
                    "Generation of high DC voltages: Half-wave and full-wave rectifier circuits, Cockcroft-Walton voltage multiplier.",
                    "Generation of high AC voltages: Cascaded transformers, resonant transformers.",
                    "Generation of impulse voltages: Single-stage and multi-stage Marx impulse generator circuits.",
                    "Generation of impulse currents, tripping and control of impulse generators."
                ]
            },
            {
                "unit": 4,
                "title": "Measurement of High Voltages & Currents",
                "topics": [
                    "Peak voltage measurements: Sphere gaps, electrostatic voltmeters.",
                    "Generating voltmeters, peak reading AC voltmeters, voltage dividers (resistive, capacitive).",
                    "Measurement of high DC, AC, and impulse currents: Hall generators, Rogowski coils, shunts."
                ]
            },
            {
                "unit": 5,
                "title": "High Voltage Testing & Insulation Coordination",
                "topics": [
                    "Testing of insulators, bushings, cables, and transformers: destructive and non-destructive tests.",
                    "Radio interference measurements, insulation coordination: statistical approach, surge arresters."
                ]
            }
        ],
        "textbooks": [
            "M.S. Naidu and V. Kamaraju, 'High Voltage Engineering', Tata McGraw-Hill, 5th Edition.",
            "C.L. Wadhwa, 'High Voltage Engineering', New Age International Publishers, 3rd Edition."
        ]
    },
    "EC702": {
        "code": "EC702",
        "title": "Radar & Satellite Communication",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Radar Equations & Types",
                "topics": [
                    "Radar basic principles, range equation, radar block diagram, operation frequencies.",
                    "Minimum detectable signal, receiver noise, radar cross-section of targets.",
                    "Pulse repetition frequency, range ambiguities, system losses.",
                    "CW and Frequency-Modulated Radar: Doppler effect, FMCW radar, altimeters."
                ]
            },
            {
                "unit": 2,
                "title": "MTI & Tracking Radar",
                "topics": [
                    "MTI radar: Delay-line cancelers, blind speeds, double cancellation, staggered PRFs.",
                    "Muser-limiter, tracking radars: Sequential lobing, conical scan, monopulse tracking (amplitude and phase)."
                ]
            },
            {
                "unit": 3,
                "title": "Satellite Orbits & Kepler's Laws",
                "topics": [
                    "Satellite history, orbital mechanics, Kepler's laws of planetary motion.",
                    "Locating the satellite in orbit, look angles (elevation and azimuth angles) calculation.",
                    "Orbital perturbations, launches and launch vehicles, geostationary orbit parameters."
                ]
            },
            {
                "unit": 4,
                "title": "Satellite Subsystems & Space Link",
                "topics": [
                    "Subsystems: Attitude and orbit control, telemetry, tracking, command, power systems, transponders.",
                    "Satellite link design: Basic transmission theory, system noise temperature, G/T ratio.",
                    "Design of downlinks and uplinks under rain fade conditions, link budgets calculations."
                ]
            },
            {
                "unit": 5,
                "title": "GPS & Satellite Services",
                "topics": [
                    "Global Positioning System (GPS): Segment organization, GPS codes, position determination.",
                    "Direct Broadcast Satellite (DBS) television, satellite internet services, VSAT networks."
                ]
            }
        ],
        "textbooks": [
            "Merrill I. Skolnik, 'Introduction to Radar Systems', Tata McGraw-Hill, 3rd Edition.",
            "Dennis Roddy, 'Satellite Communications', McGraw-Hill, 4th Edition."
        ]
    }
}
