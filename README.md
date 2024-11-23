____    __    ____  ______   .______       _______   __       _______         _______.  ______    __      ____    ____  _______ .______
\   \  /  \  /   / /  __  \  |   _  \     |       \ |  |     |   ____|       /       | /  __  \  |  |     \   \  /   / |   ____||   _  \
 \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  ||  |     |  |__         |   (----`|  |  |  | |  |      \   \/   /  |  |__   |  |_)  |
  \            /  |  |  |  | |      /     |  |  |  ||  |     |   __|         \   \    |  |  |  | |  |       \      /   |   __|  |      /
   \    /\    /   |  `--'  | |  |\  \----.|  '--'  ||  `----.|  |____    .----)   |   |  `--'  | |  `----.   \    /    |  |____ |  |\  \----.
    \__/  \__/     \______/  | _| `._____||_______/ |_______||_______|   |_______/     \______/  |_______|    \__/     |_______|| _| `._____|

This program is a helper tool for word puzzle games. It narrows down possible solutions based on your feedback and provides suggestions for the next guess.

## How to Use

1. **Run the Script**:  
   ```bash
   python word_solver.py

    Start with a Guess:
    Suggested starting words: ADIEU, SLATE, or other vowel-rich options.

    Enter Feedback:
    After each guess, input feedback based on the puzzle's response:
        1<letter>: Green (correct position).
        0<letter>: Yellow (present but wrong position).
        <letter>: Black (not in the word).

    Example:
    If you guessed SLATE and received feedback:
        S is correct (green): 1S
        L is present but misplaced (yellow): 0L
        A, T, and E are not in the word (black): A T E
        Enter the feedback as:

Enter output: 1S 0L A T E

Review Suggestions:
The program will display a list of possible words based on your input.

Repeat:
Use the suggestions to make another guess and provide feedback until the word is solved.

Solve and Exit:
Once the puzzle is solved, type:

    SOLVED

    The program will exit with a friendly message.

Example Session

    Start with a guess like ADIEU.
    Enter feedback for ADIEU:

Enter output: 1A 0D E

The program will filter and suggest possible words:

['ADEPT', 'ADORN', ...]

Continue guessing and refining until the word is solved.
Exit by typing:

    SOLVED

Notes

    Use feedback format accurately to get proper suggestions.
    Experiment with different starting words for better results.

Happy solving! 🎉