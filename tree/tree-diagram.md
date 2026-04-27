# Reflection Tree Diagram

```mermaid
graph TD

%% --- START ---
START([Start]) --> A1_OPEN

%% =========================
%% AXIS 1: LOCUS OF CONTROL
%% =========================
subgraph Axis1["Axis 1: Locus of Control (Agency)"]
A1_OPEN --> A1_D1

A1_D1 -->|Productive / Steady| A1_Q1_HIGH
A1_D1 -->|Frustrating / Draining| A1_Q1_LOW

A1_Q1_HIGH --> A1_Q2_HIGH --> A1_Q3_HIGH --> A1_D2
A1_Q1_LOW --> A1_Q2_LOW --> A1_Q3_LOW --> A1_D2B

A1_D2 --> A1_R_INT_STRONG
A1_D2 --> A1_R_INT_MID
A1_D2 --> A1_R_EXT_HINT

A1_D2B --> A1_R_EXT_STRONG
A1_D2B --> A1_R_INT_HINT
end

%% --- BRIDGE 1 → 2 ---
A1_R_INT_STRONG --> B12_1
A1_R_INT_MID --> B12_2
A1_R_EXT_STRONG --> B12_3
A1_R_EXT_HINT --> B12_4
A1_R_INT_HINT --> B12_5

%% =========================
%% AXIS 2: CONTRIBUTION
%% =========================
subgraph Axis2["Axis 2: Contribution vs Entitlement"]
B12_1 --> A2_OPEN
B12_2 --> A2_OPEN
B12_3 --> A2_OPEN
B12_4 --> A2_OPEN
B12_5 --> A2_OPEN

A2_OPEN --> A2_Q1 --> A2_Q2 --> A2_D1

A2_D1 --> A2_R_CONTRIB_STRONG
A2_D1 --> A2_R_CONTRIB_BASE
A2_D1 --> A2_R_ENTITLE
end

%% --- BRIDGE 2 → 3 ---
A2_R_CONTRIB_STRONG --> B23_1
A2_R_CONTRIB_BASE --> B23_2
A2_R_ENTITLE --> B23_3

%% =========================
%% AXIS 3: RADIUS OF IMPACT
%% =========================
subgraph Axis3["Axis 3: Radius (Self → Others → System)"]
B23_1 --> A3_OPEN
B23_2 --> A3_OPEN
B23_3 --> A3_OPEN

A3_OPEN --> A3_Q1 --> A3_Q2 --> A3_D1

A3_D1 --> A3_R_SELF
A3_D1 --> A3_R_TEAM
A3_D1 --> A3_R_COLLEAGUE
A3_D1 --> A3_R_SYSTEM
end

%% --- SUMMARY ---
A3_R_SELF --> SUMMARY
A3_R_TEAM --> SUMMARY
A3_R_COLLEAGUE --> SUMMARY
A3_R_SYSTEM --> SUMMARY

SUMMARY --> END([End])
