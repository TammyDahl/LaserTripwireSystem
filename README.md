# Laser-Based Bed Exit Detection System | CS 578 Project

## Overview
This project was developed as part of my Wireless Networks course (CS 578) at San Diego State University. It was inspired by Raspberry Pi’s [Laser Tripwire project](https://projects.raspberrypi.org/en/projects/laser-tripwire) and adapted to address a real-world healthcare need: detecting when a patient exits a bed and sending an automated alert to a caregiver.

The system uses a Raspberry Pi, laser module, and photoresistor to detect beam interruptions, with immediate notifications sent through IFTTT. While rooted in embedded systems, this project reflects my broader interest in building end-to-end technical solutions that prioritize safety, usability, and real-world application.

## Problem Statement
Patients in psychiatric care, elder care, or pediatric settings may be unable to call for help or trigger a manual alert if they leave their bed. Missed bed exits can lead to injuries or slow response times. This system offers a non-invasive and automated solution to bridge that gap—no wearables or complex monitoring infrastructure required.

## How It Works
- A laser is mounted across the bed at exit level.
- A photoresistor (LDR) on the opposite side detects whether the beam is intact.
- A Python script on a Raspberry Pi monitors the signal.
- If the beam is interrupted, an IFTTT webhook sends an alert to a phone or email in real time.

## Key Technologies
- Raspberry Pi (GPIO, Python scripting)
- Laser and photoresistor circuit
- IFTTT Webhooks for remote alerts
- Future Considerations: logging beam interruptions, adding camera-based monitoring, or dashboard integrations

## Demo
📽️ Watch the [Demo Video](https://www.youtube.com/watch?v=IfYAgOm_tNY)

## Files Included
[tripwire.py](https://github.com/TammyDahl/LaserTripwireSystem/blob/main/tripwire.py) – Main script for GPIO monitoring and IFTTT integration

[Laser Tripwire Presentation.pdf](https://github.com/TammyDahl/LaserTripwireSystem/blob/main/Laser%20Tripwire%20Presentation.pdf) – Final project slide deck

## Why I Included This in My Portfolio
While my primary interest lies in data analytics, AI, and applied data science, I believe this project shows:

- A strong understanding of system design and automation
- Comfort with scripting and hardware integration
- A practical approach to real-world problems
- The ability to own and deliver a complete solution from idea to demo

If you're hiring for a role that values technical problem-solving, real-world impact, and adaptability across tools and environments—I’d love to connect.
