# IEEE RAS Task 4 – Op-Amp Circuits

**Task Title:** Watch The Red Lights – Op-Amp as Comparator and Amplifier

**Semester / Event:** IEEE Student Branch RAS – Introductory Tasks (2023)

**Deadline:** Friday, December 8th, 2023 at 23:00

**Full Name:** Islam Elsayed  <!-- Replace with your full last name if applicable -->

**University:** Zagazig University <!-- Add your university name -->

**Department:** Electrical Engineering / Electronics  <!-- Adjust based on your department -->

## Task Objectives

- Learn about operational amplifiers (op-amps), including their use as comparators and amplifiers.
- Understand inverting/non-inverting configurations, comparators, and basic applications like light sensing with LDR.

## Resources Used

- Videos: "Intro to Op-Amps", "Inverting and Non-inverting Amplifiers", "Comparator - Operational Amplifier", "How Op Amps Work".
- Walid Issa – Electronics Playlist (Arabic).
- Proteus 8 Professional for circuit simulation.

## Task Requirements & Solutions

1. **Design Op-Amp as Comparator with LDR Voltage Divider to Control LED:**  
   Implemented using LM741 op-amp as a comparator. The LDR (TORCH_LDR) and potentiometer (RV1 1k) form a voltage divider connected to the non-inverting input (pin 3). The inverting input (pin 2) is set to a reference (e.g., via divider or ground). Output (pin 6) drives an LED (D1 LED-RED) through a current-limiting resistor (R1 220Ω). When light intensity changes LDR resistance (79% in sim), the comparator toggles the LED on/off based on threshold set by RV1.

2. **Design Op-Amp as Amplifier with Gain of 10:**  
   Designed an inverting amplifier using LM741 (U2). Input signal from VSine connected to inverting input (pin 2) via Rin (R3 1k). Feedback resistor Rf (R4 10k) from output (pin 6) to pin 2. Non-inverting input (pin 3) grounded via R2 (1k). Gain = -Rf/Rin = -10 (magnitude 10x amplification). Output labeled A B C D for probing.

All circuits are combined in a single Proteus project for simulation efficiency.

## Project Structure

```
Task4/
├── Explanation_Video.mp4          ← 3-minute video explaining all circuits and components
├── README.md                        ← This documentation file
├── Schematic_Task4.PDF              ← PDF export of the Proteus schematic
├── Task_4.pdf                       ← Original task requirements PDF
└── Task4.00.pdsprj                  ← Proteus simulation project file (all circuits in one)
```

## Circuit Descriptions

- **Comparator Circuit (Problem 1):**  
  - Components: LM741 (U1), LDR1 (TORCH_LDR), RV1 (1k pot for threshold), R1 (220Ω), D1 (LED-RED), DC power supplies (V+, V-).  
  - Operation: LDR voltage divider feeds non-inverting input. Comparator compares to reference on inverting input. High output lights LED when input > reference (e.g., in low light). Simulates light sensor switch, similar to transistor switch but with high gain for sharp transitions.

- **Amplifier Circuit (Problem 2):**  
  - Components: LM741 (U2), VSine (input signal), R3 (1k Rin), R4 (10k Rf), R2 (1k to ground non-inv).  
  - Operation: Inverting configuration amplifies input by -10. For example, 1V input gives -10V output (inverted). High input impedance, low output impedance. Useful for signal conditioning.

Simulation in Proteus confirms functionality: Adjust RV1 or light on LDR to toggle LED; apply sine wave to see amplified output.

## Key Learnings

- Op-amps have high gain, differential inputs, and are powered by dual supplies (V+, V-).
- Comparator mode: Open-loop for digital decisions (high/low output).
- Amplifier mode: Closed-loop with feedback for linear gain control.
- LDR: Resistance decreases with light, ideal for sensors.
- Always consider slew rate, bandwidth, and offset in real designs.

## How to Run the Simulation

1. Open Proteus 8 Professional.
2. Load `Task4.00.pdsprj`.
3. Click the play button to simulate.
4. Adjust RV1 or TORCH_LDR intensity to test comparator; use virtual oscilloscope for amplifier waveforms.

## Evaluation Notes

- Each Circuit: 4/4 (Total 8/8 – Both functional in simulation).
- Explanation Video: 2/2 (Covers all circuits, components, and operations).

*Submitted for IEEE SB RAS – December 2023*  
*Prepared by: Islam*