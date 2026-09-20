# Notebook 00 Physics Companion: Sonar Intuition and Baseline Parameters

This companion stands apart from the notebook code, but it follows the same
story as the notebook: start with a ping, track the echo delay, turn that
delay into samples, and then turn samples back into range. Its job is to
define the physics, the symbols, and the assumptions that make that story
work.

Read this companion first if you want the physical story in prose before you
open the notebook and work through the code.

## 1. Active sonar in one sentence

An active sonar sends a short burst of sound into the water and then listens
for the echo that returns from a target.

That sentence already contains the core physics:

- there is a transmitted wave
- the wave travels through water at a finite speed
- the target reflects some of that wave back
- the measured delay encodes range

## 2. Why sonar uses sound underwater

Water is friendly to sound compared with light and radio. In this course we use
an effective sound speed of:

- `c = 1500 m/s`

That number is slow enough that you can feel the timing. A target tens
of metres away does not return an echo in microseconds; it returns after a
noticeable fraction of a second.

The major difference between radar and sonar is the propagation speed.
Electromagnetic waves travel much faster than sound, so the same physical
distance shows up as a very different delay scale. That one change alters the
timing, the range scale, and the ping rhythm in this notebook.

## 3. The transmit-listen rhythm

An active sonar cannot transmit and listen to a weak echo at full sensitivity
at the same instant. The sonar therefore alternates between:

1. transmit
2. quiet listening

Two timing quantities define that rhythm.

### Ping width

`tau` is the duration of the transmitted pulse.

For the baseline scene:

- `tau = 0.05 s`

### Inter-ping interval

`T` is the time from the start of one ping to the start of the next.

For the baseline scene:

- `T = 0.2 s`

### Duty cycle

The duty cycle is the fraction of time spent transmitting:

$$
D = \frac{\tau}{T}
$$

With the baseline values:

$$
D = \frac{0.05}{0.2} = 0.25
$$

So the sonar is transmitting for 25% of each cycle and listening for the other
75%.

That matters physically because long transmit time can improve energy on target,
but every extra moment spent transmitting reduces the quiet time available to
hear the return.

## 4. Range from round-trip delay

The first range equation in the course is:

$$
R = \frac{c\,\tau_{delay}}{2}
$$

where:

- `R` is target range
- `c` is sound speed in water
- `tau_delay` is the measured echo delay

The factor of 2 is essential. The echo delay is a round-trip travel time:

- one trip from sonar to target
- one trip from target back to sonar

So if the target is at range `R`, the total path length is `2R`, and the delay is:

$$
\tau_{delay} = \frac{2R}{c}
$$

For the baseline target at `R = 75 m`:

$$
\tau_{delay} = \frac{2 \cdot 75}{1500} = 0.1\,s
$$

This 0.1 s delay is central to the whole early track. It is long enough to be
visible and intuitive, and it fits comfortably inside the 0.2 s ping cycle.
The notebook uses that delay in the same order the physics does: first as a
time, then as samples, and finally as range.

## 5. Delay in samples

Digital signal processing does not work directly in continuous time. It works in
samples.

For the baseline scene:

- sample rate `f_s = 10,000 Hz`

The number of samples corresponding to the round-trip delay is:

$$
N_{delay} = f_s\,\tau_{delay}
$$

Using the baseline numbers:

$$
N_{delay} = 10000 \cdot 0.1 = 1000
$$

So the first useful mental picture for you is:

- target at 75 m
- echo arrives after 0.1 s
- echo begins about 1000 samples after transmit

That same sample delay will later reappear in the channel model and matched
filter notebooks.

## 6. Why these baseline values were chosen

The baseline scene is not arbitrary. It was chosen so the first-principles
relationships stay clean across the whole course.

- `c = 1500 m/s` keeps the water physics explicit.
- `R = 75 m` gives a round-trip delay of exactly `0.1 s`.
- `f_s = 10 kHz` turns that delay into exactly `1000` samples.
- `tau = 0.05 s` and `T = 0.2 s` leave a generous listen window.

Those values make the early notebooks easy to verify by hand and keep the later
notebooks internally consistent.

## 7. What this notebook does not explain yet

Notebook 00 establishes timing and baseline geometry only. It does not yet
answer:

- why an FM sweep improves range resolution
- why the echo is weak after propagating through water
- how noise and reverberation corrupt the return
- how matched filtering sharpens the echo
- how velocity appears through Doppler

Those are deferred on purpose. The goal here is to make the first timing model
solid before adding more physics.

## 8. Summary

You should leave Notebook 00 with four durable facts:

- active sonar means ping first, then listen
- sound speed in water sets the timing scale
- measured echo delay is a round-trip quantity
- sample delay is just the same physical delay written in digital form

That is the whole arc of the notebook companion: a physical ping, a measured
delay, a sample count, and a recovered range.

Everything later in the course builds on those four facts.
