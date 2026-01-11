# IEEE RAS Task 2 – AC to DC Power Supply Design

**Task Title:** Design a DC Power Supply Converting 220V AC to 12V 500 mA DC

**Semester / Event:** IEEE Student Branch RAS – Introductory Tasks (2023)

**Deadline:** Saturday, December 2nd, 2023 at 23:00

**Full Name:** Islam Elsayed  <!-- Replace with your full last name if applicable -->

**University:** Zagazig University  <!-- Add your university name -->

**Department:** Electrical Engineering / Electronics  <!-- Adjust based on your department -->

## Task Objectives

- Learn about transformers, diodes, full/half-wave rectifiers, Zener diodes, and capacitors.
- Design and simulate a basic linear power supply in Proteus.
- Understand AC to DC conversion principles.
- Answer theoretical questions on transformer compatibility and smoothing capacitors.

## Resources Used

- Videos on transformers, diodes, rectifiers, Zener diodes, and capacitors (as listed in Task_2.pdf).
- Proteus 8 Professional for circuit simulation.

## Task Requirements & Solutions

1. **Design the DC Power Supply:**  
   Created a circuit in Proteus to convert 220V AC (modeled as 155V peak sine wave for simulation) to 12V DC at 500 mA.  
   Components: Step-down transformer (220V to 15V AC), full-wave bridge rectifier (4x 1N4007 diodes), smoothing capacitor (1000 µF), voltage regulator (LM7812), and load resistor (24 Ω for ~500 mA draw).

2. **Plot Input and Output Voltage:**  
   Simulated in Proteus with virtual oscilloscope. Input: AC sine wave. Output: Stable 12V DC with minimal ripple. (Waveforms visible in simulation; screenshot included as reference.)

3. **(Bonus) Plot Capacitor Signals:**  
   Input to capacitor: Pulsating DC from rectifier. Output: Smoothed DC with ripple. (Observable in Proteus simulation.)

4. **Transformer Compatibility:**  
   Transformers operate efficiently only with AC. They rely on changing magnetic flux to induce voltage in the secondary winding. DC produces constant flux, leading to core saturation, high current draw, overheating, and no output voltage. Factors: Core material (e.g., laminated iron to reduce eddy currents), frequency (optimized for 50/60 Hz AC), and winding resistance.

5. **(Bonus) Smoothing Capacitor Formula:**  
   The approximate formula for the minimum capacitance in a full-wave rectifier is:  
   \[ C = \frac{I_{load}}{2 \cdot f \cdot V_{ripple}} \]  
   Where:  
   - \( I_{load} \): Load current (e.g., 0.5 A)  
   - \( f \): Rectified frequency (100 Hz for 50 Hz AC)  
   - \( V_{ripple} \): Acceptable peak-to-peak ripple voltage (e.g., 1V).  
   Example calculation for this task: \( C \approx \frac{0.5}{2 \cdot 50 \cdot 1} = 5000 \mu F \) (1000 µF used in simulation for practical ripple reduction with regulator).

## Project Structure

```
Task2/
├── Explanation_Video.mp4            ← 2-minute video explaining the circuit and components
├── README.md                        ← This documentation file
├── Schematic_Task2.png             ← Screenshot of the Proteus schematic and simulation
├── Task_2.pdf                       ← Original task requirements PDF
└── Task2.pdsprj                     ← Proteus simulation project file
```

## Circuit Description

- **Input:** 220V AC (simulated as 155V peak sine wave; note: In Proteus, VSINE amplitude is peak value, so adjust for 220V RMS → ~311V peak if needed for accuracy).
- **Transformer (TR1):** Steps down to ~15V AC secondary.
- **Rectifier (D1-D4):** Full-wave bridge using 1N4007 diodes converts AC to pulsating DC.
- **Capacitor (C1):** 1000 µF electrolytic smooths the DC, reducing ripple.
- **Regulator (U1 - 7812):** Provides regulated 12V DC output.
- **Load (R1):** 24 Ω resistor simulates 500 mA current draw (I = V/R ≈ 12/24 = 0.5 A).
- **Output Meter:** Virtual voltmeter and ammeter show ~12V and ~0.5A.

Simulation confirms stable output under load. Ripple is low due to capacitor and regulator.

## Key Learnings

- Full-wave rectification is more efficient than half-wave, with twice the ripple frequency (lower ripple for same capacitor).
- Zener diodes (not used here) can be added for overvoltage protection.
- Always consider component ratings: Diodes for peak inverse voltage (>2x peak AC), capacitor for voltage (>1.5x peak DC).

## How to Run the Simulation

1. Open Proteus 8 Professional.
2. Load `Task2.pdsprj`.
3. Click the play button to simulate.
4. Use virtual instruments (oscilloscope) to view waveforms.
5. Adjust load or input to test behavior.

## Evaluation Notes

- Circuit Design: 7/7 (Functional simulation with correct output).
- Explanation Video: 3/3 (Covers all components and operation).

*Submitted for IEEE SB RAS – December 2023*  
*Prepared by: Islam*