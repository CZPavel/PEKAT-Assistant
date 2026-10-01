# Advisory workflow example

**User:** “Our inspection rejects a part that looks good. PEKAT VISION is 4.0.3. The sanitized FLOW is acquisition → Detector → boolean gate → final result. I have an evaluated image and a native-result screenshot.”

**Approach:** Identify image, active model and variant. Separate object presence, gate condition and final verdict. A module list does not prove the executed branch or output behavior.

**Useful response:** “The supplied Detector result supports object presence in this frame. The rejection may arise from the gate or a later decision; the current evidence does not establish which. Supply the gate's visible condition and evaluated branch result with identifiers redacted. Compare this frame against the intended acceptance criterion before changing thresholds.”

No project modification or runtime test occurs. A proposed check is not an observed result.
