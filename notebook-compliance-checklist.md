# Notebook compliance checklist

This checklist defines the standard every beginner notebook must meet before it is considered complete.

## Required notebook standard

Each notebook should:

1. Be readable for a beginner.
   - Clear chapter titles.
   - Short explanatory paragraphs.
   - Concrete examples before abstractions.
   - No unexplained jargon.

2. Include the necessary math and physics.
   - The relevant equation must be shown explicitly.
   - The equation must be explained in plain language.
   - The lesson must connect the equation to a physical interpretation.

3. Show the calculations in explicit cells.
   - At least one cell should compute the core quantity by hand.
   - The code should use the variables directly so the student can see the arithmetic.
   - The student should see the same formula in code and in prose.

4. Show the implementation in beginner-friendly cells.
   - The notebook should include a worked example before any helper is used.
   - The first time a concept appears, the direct implementation should be visible in the notebook itself.
   - The helper call should appear as a repetition of the same idea, not a mystery shortcut.
   - The notebook should explicitly teach the idea first and then show the packaged helper as a reusable abstraction.

5. Use shared helpers for later reuse.
   - Shared functionality belongs in the beginner helper package.
   - Later notebooks should use the helper API instead of duplicating logic.

6. Include a final summary and learning checkpoint.
   - The notebook should end by recalling the key equations and the main physical idea.
   - It should conclude with a short set of learner checks or questions.

## Required ordering for each notebook

Every notebook should follow this structure:

1. Chapter title and learning goals.
2. Short narrative framing.
3. Setup and baseline values.
4. Core model or physical idea.
5. Explicit worked calculations.
6. Helper-based implementation.
7. Output and interpretation.
8. Checkpoint, common mistakes, or reflection.
9. Summary connecting it back to the sonar story.

## Review gate

A notebook is only complete when all of the following are true:

- The notebook runs without errors.
- The math is visible and explained.
- The calculations are shown explicitly.
- The same result is reproduced by a helper function.
- The wording is written for beginners, not experts.
- The chapter fits the sequence of the course.

## Current enforcement target

The beginner track should aim for this standard across notebooks 00 through 10, with the same educational rigor throughout the full series.
