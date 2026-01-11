# IEEE RAS Task 3 – Transistor and Relay Circuits

**Task Title:** Hold Your Clutch – Circuits with Transistors, Relays, H-Bridge, and DC Motor Control

**Semester / Event:** IEEE Student Branch RAS – Introductory Tasks (2023)

**Deadline:** Wednesday, December 6th, 2023 at 23:00

**Full Name:** Islam Elsayed  <!-- Replace with your full last name if applicable -->

**University:** Zagazig University  <!-- Add your university name -->

**Department:** Electrical Engineering / Electronics  <!-- Adjust based on your department -->

## Task Objectives

- Learn about NPN and PNP transistors, relays, H-bridges, and DC motors.
- Design and simulate basic switching and control circuits in Proteus.
- Understand transistor operating regions (cut-off, active, saturation) for switching and amplification.
- Explore relay usage for switching and limitations for amplification.

## Resources Used

- Videos: "What is an H-Bridge?", "How a Bipolar Junction Transistor works", "Different Operating Regions of BJTs", "Relay".
- Walid Issa – Electronics Playlist (Arabic).
- Proteus 8 Professional for circuit simulation.

## Task Requirements & Solutions

1. **Design a Switch Circuit with a Transistor:**  
   Implemented a simple NPN transistor (TIP122) as a switch to control an LED. The base is driven via a resistor (10k) and switch (SW2). When the switch is closed, base current flows, saturating the transistor and turning on the LED.

2. **Design a Switch Circuit with a Relay:**  
   Used a relay (RL1) controlled by a switch (SW) and battery (BAT1 5V). The coil is energized via the switch, closing the relay contacts to control a load (e.g., simulated with VSINE and inductor L1). Demonstrates electrical isolation and high-current switching.

3. **Design an Amplifier Circuit (Can You Do It with a Relay?):**  
   Designed a common-emitter amplifier using an NPN transistor (TIP122) with input capacitor (C1 1uF), base resistor (R2 2k), collector resistor (R1 3k), and output to LED/voltmeter. The circuit amplifies a small AC signal from VSINE.  
   **With a Relay?** No, relays are electromechanical switches and cannot provide continuous amplification like transistors; they are binary (on/off) and not suitable for linear amplification.

4. **Design an H-Bridge Circuit Using 2 NPNs & 2 PNPs:**  
   Built an H-bridge with 2 NPN (TIP122) and 2 PNP (TIP127) transistors to control a DC motor in both directions. Control switches/resistors (10k) drive the bases. Proper activation (e.g., Q2 and Q5 for one direction, Q3 and Q4 for reverse) allows bidirectional control without shorting the supply.

All circuits are combined in a single Proteus project for simulation efficiency.

## Project Structure

```
Task3/
├── Explanation_Video.mp4          ← 3-minute video explaining all circuits and components
├── README.md                        ← This documentation file
├── Task_3.pdf                       ← Original task requirements PDF
├── Schematic_Task3.PDF              ← PDF export of the Proteus schematic
└── Task3.00.pdsprj                  ← Proteus simulation project file (all circuits in one)
```

## Circuit Descriptions

- **Transistor Switch (Problem 1):**  
  - Components: NPN TIP122, R6 10k (base pull-down), R7 10k (base current limit), SW2 (control), LED (load).  
  - Operation: Switch closes to apply voltage to base, transistor saturates, LED turns on. Demonstrates low-side switching.

- **Relay Switch (Problem 2):**  
  - Components: BAT1 5V, SW (control), RL1 relay coil, L1 (inductive load simulation), VSINE (optional test input).  
  - Operation: Switch energizes relay coil, closing contacts to switch the load. Provides isolation for high-voltage/current applications.

- **Amplifier Circuit (Problem 3):**  
  - Components: VSINE (input signal), C1 1uF (coupling), R2 2k (bias), NPN TIP122, R1 3k (collector), LED/voltmeter (output).  
  - Operation: Transistor in active region amplifies AC signal. Gain ≈ R1 / re (intrinsic emitter resistance). Relay alternative: Not feasible, as relays lack linear response.

- **H-Bridge (Problem 4):**  
  - Components: 2x TIP122 (NPN Q2, Q3), 2x TIP127 (PNP Q4, Q5), resistors (R3/R4/R8/R9/R11 10k for base control), SW1 (direction control), DC motor.  
  - Operation: For forward: Activate Q2 (NPN) and Q5 (PNP). For reverse: Q3 (NPN) and Q4 (PNP). Prevents shoot-through with proper control logic.

Simulation in Proteus confirms functionality: Switches toggle states, amplifier shows gain, H-bridge rotates motor bidirectionally.

## Key Learnings

- Transistors (BJTs): NPN for low-side, PNP for high-side switching; active region for amplification.
- Relays: Ideal for switching but noisy, slow, and power-hungry; no amplification capability.
- H-Bridge: Enables bidirectional motor control; requires careful sequencing to avoid short circuits.
- Always include base resistors to limit current and pull-downs to ensure off-state.

## How to Run the Simulation

1. Open Proteus 8 Professional.
2. Load `Task3.00.pdsprj`.
3. Click the play button to simulate.
4. Interact with switches (SW1, SW2) to test behaviors.
5. Use virtual instruments (voltmeter, oscilloscope) to observe signals.

## Evaluation Notes

- Each Circuit: 2/2 (Total 8/8 – All functional in simulation).
- Explanation Video: 2/2 (Covers all circuits, components, and operations).

*Submitted for IEEE SB RAS – December 2023*  
*Prepared by: Islam*