# COMS W3132 Individual Project
## Author
Ken Kidangalil kenkidangalil@gmail.com/kmk2255@columbia.edu
## Project Title
Snake Arcade Game
## Project Description
For my project I would like to create a simple version of the classic arcade game Snake. I am very new to using python and coding in general so I wanted to choose a project that seemed familiar, doable, but also interesting. I remember that whenever I was bored and I had access to a computer I would open the game snake and see how far I could get. It was a great way to kill time. I am also a huge gamer and I have always wondered about the amazing coding work that goes on behind the scenes of a game. I think this project will really help me develop some great practical skills in python and coding that I will definitely be able to apply in my future career and elsewhere. I hope that by the end of this project I feel more fluent in using git and python and that I understand the workflow and environments that I will be working in. I am excited and looking forward to working on this project as it will help me understand the process that goes behind creating even such a simple game like Snake. I think it will help me appreciate video games even more.

# Snake

This is a simple version of the classic arcade game Snake, implemented using the PyGame framework. The aim of this project is to create a fun and interactive Snake game.

## How to Play

### Game Objective
The objective of the game is to control the snake to eat as many food items as possible. Each time the snake eats a food item, it grows longer. The game ends when the snake collides with the walls or itself.

### Starting the Game
1. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the directory where your project is located:
     ```bash
     cd path/to/your/project/Snake
     ```

2. **Activate the Virtual Environment**:
   - On Unix-like systems (Linux, macOS):
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Run the Game Script**:
   - Start the game by running the following command:
     ```bash
     python main.py
     ```

4. **Game Window**:
   - A game window will open, displaying the initial game screen.

### Controls
- **Arrow Keys**: Use the arrow keys on your keyboard to control the direction of the snake.
  - **Up Arrow**: Move the snake upward.
  - **Down Arrow**: Move the snake downward.
  - **Left Arrow**: Move the snake to the left.
  - **Right Arrow**: Move the snake to the right.

### Scoring
- **Eating Food**: Each time the snake eats a food item, your score increases by one point.
- **Score Display**: Your current score is displayed at the top of the game window.

### Game Over
- The game ends if the snake collides with the walls or its own body.
- When the game is over, the final score is displayed.

### Restarting the Game
- To restart the game, close and reopen the game window or run the game script again.

Enjoy playing the game and try to beat your high score!

## Project Scope

### Game Version
- **One-player game:** The initial version of the game will be a single-player experience.

### Game Interface
- **GUI Game:** The game will utilize the PyGame framework to create a graphical user interface. This will allow for interactive gameplay with visual elements.

### Features
- **In Scope:**
  - Snake movement control using keyboard inputs.
  - Growing snake length upon consuming food.
  - Collision detection with walls and the snake's own body.
  - Score tracking.
  - Basic game loop with start and game-over screens.

- **Out of Scope:**
  - Two-player mode.
  - Complex AI for snake movement.
  - Online leaderboards.

### Game Architecture
- **Main Classes/Functions:**
  - `Game`: Manages the main game loop, event handling, and game states (start, playing, game over).
  - `Snake`: Represents the snake, handles movement, growth, and collision detection.
  - `Food`: Represents the food object, handles random placement on the game board.
  - `ScoreBoard`: Manages the display and updating of the score.

### Leaderboard
- **Leader Board:** The initial version will not include a leaderboard. This feature might be considered for future versions.

## Timeline
*To track progress on the project, we will use the following intermediate
milestones for your overall project. Each milestone will be marked with a tag in
the git repository, and we will check progress and provide feedback at key
milestones.*
| Date | Milestone
| Deliverables | Git tag |
|--------------------|-------------------------------------------------------------
-------------------------------------------|-------------------------------------|-
-----------|
| **July&nbsp;15** | Submit project description
| README.md | proposal |
| **July&nbsp;17** | Update project scope/direction based on instructor/TA
feedback | README.md
| approved |
| **July&nbsp;22** | Basic project structure with empty functions/classes
(incomplete implementation), architecture diagram | Source code, comments, docs
| milestone1 |
| **August&nbsp;2** | More or less complete implementation. The goal is to have
something you can share with others. | Source code, unit tests
| milestone2 |
| **August&nbsp;9** | Complete implementation. Final touches (conclusion,
documentation, testing, etc. | Source code, Conclusion
(README.md) | conclusion |
*The column Deliverables lists deliverable suggestions, but you can choose your
own, depending on the type of your project.*
## Requirements, Features and User Stories
### 1. Snake Movement Control
**Feature Description**: The player can control the movement of the snake using the arrow keys.

**User Story**: 
As a player, I want to be able to control the direction of the snake using the arrow keys so that I can navigate the snake to collect food and avoid collisions.

**Scenario**:
- The player starts the game.
- The player presses the right arrow key, and the snake moves to the right.
- The player presses the down arrow key, and the snake moves downward.
- The player continues to use the arrow keys to control the snake's direction.

### 2. Growing Snake Length Upon Consuming Food
**Feature Description**: The snake's length increases each time it consumes food.

**User Story**: 
As a player, I want the snake to grow longer each time it eats food so that the game becomes more challenging as the snake grows.

**Scenario**:
- The player navigates the snake to the food item.
- The snake eats the food, and its length increases by one segment.
- A new food item appears at a random location on the game board.

### 3. Collision Detection with Walls and Snake's Own Body
**Feature Description**: The game detects when the snake collides with the walls or its own body, resulting in a game-over state.

**User Story**: 
As a player, I want the game to end if the snake collides with the walls or its own body so that there is a challenge to avoid these obstacles.

**Scenario**:
- The player navigates the snake around the game board.
- The snake collides with the wall, and the game ends, displaying a game-over screen.
- Alternatively, the snake collides with its own body, and the game ends similarly.

### 4. Food Placement
**Feature Description**: Food items appear at random locations on the game board.

**User Story**: 
As a player, I want food to appear at random locations on the game board so that I can navigate the snake to eat the food and grow.

**Scenario**:
- The player starts the game, and a food item appears at a random location.
- After the snake eats the food, a new food item appears at another random location.
- The process repeats, providing a continuous challenge for the player.

### 5. Score Tracking
**Feature Description**: The game tracks and displays the player's score based on the number of food items consumed by the snake.

**User Story**: 
As a player, I want to see my score increase each time the snake eats food so that I can track my progress and aim for a higher score.

**Scenario**:
- The player starts the game with a score of zero.
- The snake eats a food item, and the score increases by one.
- The score is displayed on the screen, updating each time the snake eats more food.

### 6. Basic Game Loop with Start and Game-Over Screens
**Feature Description**: The game includes a main game loop with start and game-over screens.

**User Story**: 
As a player, I want a start screen to begin the game and a game-over screen when the game ends so that I have a clear start and end to each game session.

**Scenario**:
- The player launches the game and sees the start screen.
- The player presses a key to start the game, and the main game loop begins.
- When the snake collides with a wall or its own body, the game ends, and the game-over screen is displayed.
- The player can then restart the game or exit.
## Technical Specification
### Main Algorithms and Libraries Used

#### PyGame Library
**Description**: PyGame is a set of Python modules designed for writing video games. It provides functionalities such as creating windows, drawing shapes, handling events, and updating the display.

**Choice Justification**: PyGame was chosen because it simplifies many aspects of game development, allowing for focus on game logic rather than low-level details like rendering and input handling. Its robust community and extensive documentation make it a great choice for beginners and intermediate developers.

**How It Helps**: PyGame handles the graphical display, keyboard inputs, and game loop, making it easier to implement the Snake game. It provides built-in functions to draw shapes, manage frame rates, and handle events, which are essential for creating an interactive game.

#### Main Game Loop
**Algorithm Description**: The main game loop is a fundamental part of the game, responsible for continuously updating the game state and rendering the graphics.

**Choice Justification**: A structured game loop ensures that the game updates and renders at a consistent rate, providing a smooth gameplay experience.

**How It Helps**: The game loop manages the timing of game events, such as moving the snake, checking for collisions, and updating the display. It keeps the game running and responsive to user inputs.

#### Snake Movement Algorithm
**Algorithm Description**: The snake's movement is controlled based on the user's keyboard inputs. The algorithm updates the snake's position and checks for collisions with walls, food, and itself.

**Choice Justification**: Handling movement and collision detection is crucial for the game's functionality. The algorithm ensures that the snake moves predictably and that the game responds correctly to user inputs.

**How It Helps**: This algorithm allows the snake to change direction based on arrow key inputs and move smoothly across the game board. It also ensures that collisions are detected accurately, triggering game-over states or growing the snake as appropriate.

#### Random Food Placement
**Algorithm Description**: The food is placed at random positions on the game board each time the snake eats it.

**Choice Justification**: Random placement keeps the game challenging and unpredictable, requiring the player to navigate the snake to different locations.

**How It Helps**: By placing food at random locations, the game remains engaging and prevents the player from predicting the food's location, thus maintaining the challenge.

#### Score Tracking
**Algorithm Description**: The score tracking algorithm updates the player's score each time the snake eats food and displays it on the screen.

**Choice Justification**: Tracking the score provides a way to measure progress and success in the game, motivating the player to achieve higher scores.

**How It Helps**: This algorithm keeps the player informed of their performance and progress, adding a competitive element to the game.
## System or Software Architecture Diagram
*Architecture Diagram Included as a .txt file in project directory*
## Development Methodology
### Development Plan

1. **Initial Setup**:
   - Set up the project repository.
   - Create the basic project structure with initial empty or partially implemented classes and functions.
   - Create an architecture diagram to visualize the project's structure.

2. **Incremental Development**:
   - Implement each feature incrementally, starting with the core functionalities:
     - Implement the main game loop.
     - Develop the snake's movement control.
     - Implement food placement and growth mechanics.
     - Add collision detection for walls and the snake's body.
     - Implement score tracking and display.
   - Test each feature manually after implementation to ensure it works as expected.
3. **Testing and Evaluation**:
   - **Manual Testing**:
     - Test the game manually after implementing each feature to verify its functionality.
     - Check for any bugs or unexpected behavior during gameplay.
     - Ensure the game's performance is smooth and responsive to user inputs.
## Potential Challenges and Roadblocks
*I am very much a beginner when it comes to coding in Python. I went into this project knowing it would be quite a challenge to even just figure out what project to pick since I don't have much experience with coding. But when I looked at the project ideas list, the games section stood out to me immediately. I have always been and always will be a gamer, and the Snake game is probably one of the first games I remember playing in elementary school on those old Dell computers in the computer lab. It's such a simple game, but it's extremely challenging and addictive at the same time. I honestly was very worried about tackling this problem since I had never even thought about making a game from scratch by coding. It was intimidating, and that was the first major roadblock I faced. On top of that, due to my terrible work/life schedule, my plan to do this project consisted of setting aside a full day around the milestone due dates dedicated to just working on this project, which is why I only have a couple of commits where a lot has been done. Thankfully, there are a lot of powerful resources online that helped me understand this project and the workflow I needed to follow to get it done. I definitely had to use ChatGPT to help me understand the code, the algorithms, the PyGame library, and even just the basic structure of how I was using JupyterLab, the terminal, and Git to form the basis of this project. It took a few FULL days of working, reading, and understanding to be able to develop this simple project, which makes me even more grateful for the amazing games that I play daily.*
## Conclusion and Future Work
*Although this project stressed me out intensely, I am very happy with how it turned out and how well the game works. Some things I would look into adding are listed below. These features are definitely out of the scope of what I can do right now but would be very cool to see implemented.*
1. **Two-Player Mode**:
   - Introduce a two-player mode where two players can compete on the same game board with separate snakes and controls.

2. **Enhanced Graphics and Animations**:
   - Improve the visual aesthetics of the game by adding smoother animations, textures, and graphical effects.

3. **Advanced AI for Snake Movement**:
   - Implement AI-controlled snakes that provide additional challenges and dynamic gameplay.

4. **Power-Ups and Obstacles**:
   - Add various power-ups that provide temporary benefits to the player and obstacles that increase the difficulty of the game.

5. **Online Leaderboards**:
   - Integrate online leaderboards to allow players to compete globally and share their high scores.

6. **Sound Effects and Music**:
   - Enhance the gaming experience with background music and sound effects for actions such as eating food and collisions.

7. **Customizable Settings**:
   - Allow players to customize game settings, such as snake speed, board size, and control sensitivity.

