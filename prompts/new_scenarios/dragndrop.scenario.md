# Drag and Drop Testing Scenarios

## Element Overview
The Drag and Drop element has two variations: Boxes and Images.

## Requirements Summary

### Boxes
- Two squares on page (drop zone and draggable element)
- Bottom square is draggable
- Drag bottom square to top square
- On successful drop: "Dropped!" text appears in top square
- Bottom square can only be dragged once

### Images
- Two squares on page  
- Bottom square contains smiley image
- Smiley is draggable
- Smiley can be dragged between squares infinite times
- On drop: "Dropped!" text appears in the square
- Square without smiley is completely empty

---

## Test Cases

### Boxes - Positive Tests
1. **Identify draggable element**: Locate bottom square
   - Expected: Bottom square is visually distinct/markable as draggable

2. **Drag to drop zone**: Drag bottom square to top square
   - Expected: Drag operation initiates without error

3. **Drop in target zone**: Complete drag to top square
   - Expected: "Dropped!" text appears in top square

4. **Verify drop completion**: Check top square content
   - Expected: Text "Dropped!" is displayed

5. **Verify bottom square state after drop**: Check bottom square after drop
   - Expected: Appropriate state change (disabled, hidden, or marked as used)

6. **No second drag**: Attempt to drag bottom square again
   - Expected: Cannot drag again (one-time use)

7. **Refresh and retry**: Verify constraint after page elements reset
   - Expected: Constraint behavior maintained

### Boxes - Negative Tests
1. **Drag to wrong location**: Drag bottom square to area outside top square
   - Expected: Drop does not occur, text doesn't appear, element returns or stays

2. **Drag without release**: Start drag but don't complete
   - Expected: No drop occurs, element returns to original position

3. **Drag after first drop**: Attempt to drag bottom square again after first drop
   - Expected: Cannot drag (one-time constraint)

4. **Drag top square**: Try to drag the top (drop zone) square
   - Expected: Top square cannot be dragged

5. **Drag to empty space**: Drag bottom square away from target
   - Expected: Element returns to original position, no "Dropped!" appears

6. **Partial drag into zone**: Drag overlapping into zone but not fully
   - Expected: Behavior defined (may require full overlap)

### Boxes - Omitted Tests (Suggested)
1. Mouse vs touch drag behavior
2. Drag acceleration/velocity effects
3. Visual feedback during drag (shadows, opacity)
4. Snap-to-grid behavior
5. No overflow when dragging off screen
6. Drag ghost/cursor change during drag
7. Multiple boxes/drag operations
8. Browser developer tools manipulation
9. Accessibility for keyboard users (Tab + Spacebar)
10. Animation on drop completion
11. Hover states during drag
12. Drag start/end event timing

---

### Images - Positive Tests
1. **Identify smiley element**: Locate smiley in bottom square
   - Expected: Smiley image visible and distinct

2. **Drag smiley to top square**: Drag smiley from bottom to top square
   - Expected: Drag operation succeeds

3. **Drop smiley in top square**: Complete drag to top square
   - Expected: "Dropped!" text appears in top square

4. **Smiley moves with drag**: Verify smiley follows mouse during drag
   - Expected: Visual feedback of smiley being dragged

5. **Smiley in new location**: After drop, smiley should be in top square
   - Expected: Smiley is now visible in top square

6. **Drag smiley back**: Drag smiley from top square back to bottom
   - Expected: Drag operation succeeds

7. **Smiley returns to bottom**: Drop smiley back in bottom square
   - Expected: Smiley in bottom square, "Dropped!" appears

8. **Multiple drag cycles**: Repeat dragging smiley multiple times between squares
   - Expected: Each cycle works (infinite dragging support)

9. **Empty square verification**: After moving smiley, verify empty square
   - Expected: Square without smiley is completely empty (no trace)

10. **Verify bottom square initially has smiley**: Load page
    - Expected: Smiley is in bottom square initially

### Images - Negative Tests
1. **Drag to wrong location**: Drag smiley outside any square
   - Expected: Smiley returns to original square/position

2. **Drag incomplete drop**: Start drag but release in wrong area
   - Expected: Smiley returns to original position

3. **Drag without smiley**: Try to drag top square (which has no smiley)
   - Expected: Cannot drag empty square (no smiley to drag)

4. **Multiple smileys**: Verify only one smiley exists
   - Expected: Only one smiley present (no duplication on drag)

5. **Partial overlap drop**: Drop smiley with partial overlap
   - Expected: Behavior defined (may require full overlap in zone)

6. **Rapid successive drags**: Drag smiley quickly multiple times
   - Expected: Handles rapid interactions gracefully

### Images - Omitted Tests (Suggested)
1. Smiley animation during drag
2. Drop zone highlight during drag
3. Smiley hover effects
4. Mobile touch vs mouse drag
5. Ghost image during drag
6. Accessibility (keyboard drag equivalent)
7. Drag to multiple zones simultaneously
8. Smiley scale/rotation during drag
9. Performance with rapid drags
10. Browser compatibility for drag operations
11. Visual drop zone indicators
12. History/undo of drags
13. Drag outside viewport handling
14. Multiple smiley support (if applicable)
15. Smiley z-index during drag
