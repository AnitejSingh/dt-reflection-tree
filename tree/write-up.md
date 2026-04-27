# Deterministic Reflection Tree — Design Write-up

## 1. Overview

This project implements a deterministic end-of-day reflection tool that guides an employee through a structured sequence of questions across three psychological axes:

1. Locus of Control (Agency)
2. Orientation (Contribution vs Entitlement)
3. Radius (Self vs Others vs System)

The goal is not to evaluate performance, but to help the user **notice patterns in how they showed up during the day**. The system is fully deterministic: every question has fixed options, every option leads to a predefined path, and the same inputs always produce the same outputs.

---

## 2. Design Philosophy

The core idea behind the design is that **reflection is most effective when it is structured but non-judgmental**.

Instead of asking open-ended questions, the tree:
- Forces concrete choices (fixed options)
- Maps those choices to behavioral patterns
- Surfaces insights through reflections

The system is designed to feel like a **guided internal dialogue**, not a survey or a diagnostic test.

---

## 3. Axis Design and Question Rationale

### Axis 1: Locus of Control (Victim vs Victor)

Inspired by the work of :contentReference[oaicite:0]{index=0} and :contentReference[oaicite:1]{index=1}, this axis captures whether the user perceives themselves as:
- Acting on situations (internal locus), or
- Being acted upon (external locus)

#### Design Approach:
Questions focus on **observable behavior**, not self-perception.

Example patterns captured:
- Adapting vs waiting
- Acting vs reacting
- Awareness of choice vs lack of perceived control

#### Why multiple questions:
A single question is often misleading. The tree uses three:
1. Initial reaction
2. Actual behavior
3. Awareness of choice

This creates a more reliable signal of agency.

---

### Axis 2: Orientation (Contribution vs Entitlement)

Inspired by research on psychological entitlement and organizational citizenship behavior, this axis explores whether the user is focused on:
- What they gave (contribution), or
- What they deserved or expected (entitlement)

#### Design Approach:
Questions are centered around **real interactions**, not abstract beliefs.

Example distinctions:
- “Being useful” vs “getting acknowledgment”
- “Doing more than required” vs “others should do more”

#### Key Insight:
Entitlement is often invisible to the person experiencing it.  
So instead of asking directly, the tree surfaces it indirectly through:
- Expectations
- Frustration patterns
- Retrospective framing

---

### Axis 3: Radius (Self → Others → System)

Inspired by later work of :contentReference[oaicite:2]{index=2} and perspective-taking research, this axis captures the **scope of awareness**:

- Self-focused → “My work, my stress”
- Team-aware → “Our shared outcomes”
- Other-aware → “Specific individuals”
- System-aware → “End users / broader impact”

#### Design Approach:
Questions progressively widen perspective:
1. Who comes to mind?
2. How far did thinking extend?
3. What feels true in hindsight?

This allows the user to **re-evaluate their own perspective**, not just report it.

---

## 4. Branching Logic and Determinism

The tree uses:
- Decision nodes for routing
- Signals to track axis tendencies
- Threshold-based conditions for reflections

Example:
- Multiple answers tagged `axis1:internal` increase internal score
- Reflections depend on dominant signal patterns

#### Trade-off:
Instead of deep branching trees, I used:
- Moderate branching depth
- Strong signal accumulation

This keeps the system:
- Interpretable
- Maintainable
- Deterministic

---

## 5. Reflection Design

Reflections are designed to:
- Reframe, not judge
- Acknowledge reality
- Highlight unnoticed patterns

They avoid:
- Prescriptive advice
- Moral language (“should”, “good/bad”)
- Overgeneralization

Tone target:
> A thoughtful colleague helping you see something you missed

---

## 6. Trade-offs Made

### 1. Depth vs Complexity
- Added 3 questions per axis for better signal
- Avoided excessive branching to maintain clarity

### 2. Precision vs Usability
- Options are specific enough to differentiate behavior
- But still simple enough to choose quickly at the end of the day

### 3. Determinism vs Personalization
- No dynamic text generation
- Personalization achieved through:
  - branching
  - signal-based summaries
  - answer interpolation

---

## 7. What I Would Improve With More Time

1. **Richer summary generation**
   - Combine specific answers into more personalized reflections

2. **Adaptive depth**
   - Allow shorter or longer flows depending on user engagement

3. **Better signal weighting**
   - Not all answers are equally indicative; weighting could improve accuracy

4. **Longitudinal tracking**
   - Track patterns across days to surface trends

---

## 8. Conclusion

This system demonstrates how a subjective domain like reflection can be translated into a **structured, deterministic decision tree** without relying on LLMs at runtime.

The key challenge was not technical implementation, but:
- Designing meaningful distinctions
- Encoding psychological insight into fixed options
- Maintaining a natural conversational flow

The final result is a system that is:
- Predictable
- Interpretable
- Psychologically grounded
- Practically usable
