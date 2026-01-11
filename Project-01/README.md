# IEEE RAS Phase 1 Final Project – Release The Clutch!
![IEEE RAS Banner](https://img.shields.io/badge/IEEE-RAS%20Phase%201-blue?style=for-the-badge&logo=ieee)  
![Completion Badge](https://img.shields.io/badge/Phase%201-100%25%20Complete-green?style=for-the-badge)  
![University](https://img.shields.io/badge/University-Zagazig%20University-orange?style=flat-square)

**Project Title:** Release The Clutch! – Traffic Light and IR Module Circuits

**Group ID:** E (Phoenix Team)

**Semester / Event:** IEEE Student Branch RAS – Introductory Phase 1 Projects (2023/2024)

**Presentation Date:** Specified date after submission deadline (as per project guidelines)

**Team Members:**
- Hager Ahmed Mohamed
- Hager Mohamed Sobhy
- Eman Atef Khodary
- Tasneem Ashraf Elsayed
- Islam Elsayed Mohamed
- Ziad Ahraf Essa
- Ahmed Yasser

**University:** Zagazig University

**Department:** Electrical Engineering / Electronics

## Project Overview

This project serves as the capstone for Phase 1 of the IEEE RAS introductory tasks, focusing on applying electronics basics learned from previous tasks (e.g., timers, op-amps, transistors). As a team of 7 members (Phoenix Team, Group E), we designed, simulated, and physically implemented two circuits:

1. **Single Traffic Light Circuit:** Using a 555 timer for timing and a CD4017 counter for sequential LED control.
2. **IR Module Using Op-Amp:** An infrared sensor module with LM358 comparator for object detection.

The circuits were built with physical components (bonus: avoiding batteries where possible by using alternative power sources like adapters). We presented our work in a group presentation, ensuring every member participated, with detailed explanations of inputs, outputs, components, calculations, timings, and documentation via videos/pictures.

**Bonus Achievement:** Batteries are lava! – We prioritized efficient designs to minimize power draw and used regulated supplies in simulations/hardware.

## Project Objectives

- Practice fundamentals of electronics, including timing circuits, counters, comparators, and sensors.
- Collaborate in sub-teams to design functional circuits.
- Implement simulations in Proteus and hardware prototypes.
- Document everything in a comprehensive presentation, including calculations and real-world demos.

## Resources Used

- Previous RAS tasks (e.g., 555 timers from Task 5, op-amps from Task 4).
- Walid Issa – Electronics Playlist (Arabic).
- Online tutorials on 555 timers, CD4017 counters, LM358 op-amps, and IR sensors.
- Proteus 8 Professional for simulations.
- Physical components: LEDs, resistors, capacitors, diodes, 555 IC, CD4017 IC, LM358, IR photodiode pair, potentiometer, 9V battery/adapter.

## Project Requirements & Solutions

1. **Single Traffic Light Circuit:**
   - **Design:** A sequential controller simulating traffic lights (red, yellow, green) using 555 timer in astable mode for clock pulses and CD4017 decade counter for sequencing.
   - **Simulation:** Implemented in Proteus; pulses generate timed LED transitions.
   - **Hardware:** Built with physical components; video demo shows cycling lights.
   - **Calculations:** Pulse period T = 0.694 * (R1 + 2*R2) * C ≈ 0.694 * (10k + 2*100k) * 10µF = 1.45 seconds per clock. Red: 5 clocks (7.25s), Yellow: 2 clocks (2.9s), Green: 3 clocks (4.35s).
   - **Operation:** Timer generates pulses; counter activates outputs sequentially, connected to LEDs via diodes for one-way control.

2. **IR Module Using Op-Amp:**
   - **Design:** Comparator-based sensor with IR LED transmitter and photodiode receiver; LM358 compares voltages to detect objects.
   - **Simulation:** In Proteus; adjustable threshold via 1k pot; LED indicates detection.
   - **Hardware:** Physical build; video shows LED activating on object proximity.
   - **Calculations:** Reference voltage adjustable (0-5V via pot); IR reflection increases non-inverting input voltage, triggering high output when > reference. Current limiting: R=220Ω for LED (I≈(5V-1.8V)/220≈14mA).
   - **Operation:** IR light reflects off objects to photodiode, increasing voltage; comparator toggles LED. Closer object → stronger signal → higher voltage.

Both circuits were tested for functionality, with hardware avoiding direct battery dependency where possible (e.g., using USB adapters for demos).

## Project Structure

```
Project1/
├── IR-module.MOV                    ← Hardware video demo of IR module in action
├── Traffic-light-circuit.MP4        ← Hardware video demo of traffic light cycling
├── IR module.pdsprj                 ← Proteus simulation file for IR module
├── Project 1 - Group E.pptx         ← Group presentation slides (includes schematics, calculations, photos/videos)
├── Project_I.pdf                    ← Original project requirements PDF
├── README.md                        ← This documentation file
└── trafficlight.pdsprj              ← Proteus simulation file for traffic light circuit
```

**Note on Embedded Media in PPTX:** The presentation includes 14 images (schematics, component photos, team pics) and 2 videos (circuit demos). Extract if needed for viewing.

## Circuit Descriptions & Calculations

### 1. Traffic Light Circuit
- **Components:** 555 timer, CD4017 counter, 3 LEDs (red/green/yellow), 6x 1N4148 diodes, 10µF capacitor, resistors (220Ω, 10kΩ, 100kΩ), 9V supply.
- **Schematic:** (From PPTX – Top: Timer pulse generator; Bottom: Counter with LED outputs.)
- **Working Principle:** 555 in astable mode generates clock pulses. CD4017 counts pulses and activates Q0-Q9 outputs sequentially. Diodes ensure unidirectional flow. LEDs light in order: Green (Q0-Q2), Yellow (Q3-Q4), Red (Q5-Q9), then reset.
- **Timing Calculation:** 
  - Frequency f = 1/T ≈ 0.69 Hz.
  - Green: 3 pulses ≈ 4.35s; Yellow: 2 pulses ≈ 2.9s; Red: 5 pulses ≈ 7.25s.
  - Total cycle: 10 pulses ≈ 14.5s.
- **Power Considerations:** Low-power LEDs; efficient for battery avoidance.

### 2. IR Module
- **Components:** IR photodiode pair, LED (indicator), LM358 op-amp, 1k potentiometer, resistors (100Ω, 220Ω, 10kΩ), 9V supply.
- **Schematic:** (From PPTX – IR emitter/receiver to op-amp inputs; output to LED.)
- **Working Principle:** IR LED emits light; reflection hits photodiode, generating voltage. LM358 (comparator) compares to pot-set reference: Non-inv > Inv → High output → LED ON.
- **Sensitivity Calculation:** 
  - Photodiode voltage drop: ≈0.7V threshold.
  - Gain: Open-loop (high for sharp switching).
  - Detection range: Adjustable via pot; tested up to 10-20cm depending on object reflectivity.
- **Power Considerations:** Low-current IR (≈10mA); suitable for regulated supplies.

## Key Learnings & Challenges

- **Integration:** Combined concepts from Tasks 2-5 (rectifiers/power, transistors/relays, op-amps, timers).
- **Teamwork:** Divided roles – design (Islam, Ziad), simulation (Hager A., Eman), hardware (Hager M., Tasneem), presentation (Ahmed).
- **Challenges:** Timing accuracy in hardware (capacitor tolerances); IR sensitivity to ambient light – mitigated with shielding.
- **Bonus Insight:** Avoiding batteries taught efficient design; used lab power supplies for demos.
- **Real-World Applications:** Traffic control systems; proximity sensors in robotics.

## How to View/Run

- **Simulations:** Open .pdsprj files in Proteus 8 Professional. Run simulation; interact with virtual components (e.g., adjust pot, observe LEDs).
- **Hardware Videos:** Play .MOV/.MP4 for real demos.
- **Presentation:** Open .pptx in PowerPoint; view embedded media for full experience.
- **Schematics/Calculations:** Detailed in PPTX slides.

## Evaluation Notes

- Circuit Designs: Fully functional (simulation + hardware).
- Presentation: Comprehensive, with all members participating; includes inputs/outputs, components, calculations, timings, videos/photos.
- Bonus: Achieved battery avoidance in demos.

*Submitted for IEEE SB RAS – Phase 1 Capstone (December 2023)*  
*Prepared by Phoenix Team (Group E) – Led by Islam Elsayed*  
🚦🔦 Let's release the clutch and accelerate into Phase 2! 🚀