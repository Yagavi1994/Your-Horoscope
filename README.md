# YOUR HOROSCOPE
This application is designed to provide users with insightful zodiac traits and daily horoscopes based on their chosen zodiac sign and day.

![Site view](assets/readme_images/your_horoscope.png)

The link to the live version of the project can be found [HERE](https://your-horoscope-c561ace553fc.herokuapp.com/)

## Tabel of Contents
+ [User Experience](#user-experience "User Experience")
+ [Design](#design "Design")
+ [Features](#features "Features")
+ [Testing](#testing "Testing")
+ [Technologies Used](#technologies-used "Technologies Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
 
## User Experience

### First time player:

- As a first-time user, I want to be able to determine my zodiac sign based on my month of birth. So that I can engage with content that is relevant to me without prior knowledge of astrology. 
- As a first-time user, I want to choose my zodiac sign from a list. So that I can see specific insights related to my sign.
- As a first-time user, I want the app to be colorful, have images, animations and engaging. So that my experience learning about my zodiac traits is fun and visually appealing.
- As a first-time user, I want to choose the day for which I want to know my horoscope. So that I can get insights for specific days, past, present or future.
- As a first-time user, I want easy options to navigate back or exit the app. So that I can have a smooth user experience without feeling stuck in any part of the app.
- As a first-time user, I want to see an attractive logo when I open the app. So that I can easily recognize and remember the app.
- As a first-times user, I would like a personalized feel of my name being used inside the application.
- As a first-times user, I would like a simple and clear options to enhance usability and reduce confusion.
- As a first time user, I would like to see some confirmation if I have successfully exited out of the application.
- As a first time user I would like clear instructions and feedback to rectify if I make any mistake.

### Frequent Player:

- As a frequent user, I want the horoscopes to be updated daily. So that I can rely on the app for fresh and relevant astrological insights every day.
- As a frequent user, I want to check not only my horoscope but also those of my friends and family without restrictions. So that I can share and discuss these insights with them.
- As a frequent user, I want the process of selecting zodiac signs and fetching results to be quick and simple. So that I can enjoy a seamless experience without unnecessary delays.
- As a frequent user, I want to see some animations while waiting for results. So that the waiting time is more enjoyable and the app feels lively.
- As a frequent user, I want to create a profile where I can save my zodiac sign and view past results. So that I can have a personalized experience and easily access historical datas.

## Design

### Flowchart:

I made a flowchart for the project to plan out my code structure using [Lucid](https://rb.gy/7i0nms)

![Flowchart](assets/readme_images/flowchart.png)

## Features

### Existing Features

#### Landing Page:

##### Objective:

Welcome the user to the application and collect their name for a personalized experience.

##### Design Elements:

- Logo: Placed prominently at the top, the logo serves as a visual anchor and brand identifier, ensuring it's memorable and recognizable.
- Welcome Message: A friendly and inviting message that greets users and sets a warm tone for their interaction with the application.
- Name Input: A text box prompts users to enter their name, allowing for personalization of the experience. This is optional, and users can press enter to proceed anonymously if they prefer privacy.

##### User Flow:

- User sees the logo and reads the welcome message.
- User is prompted to enter their name for a personalized experience or can choose to proceed without doing so by pressing enter.
- Upon submission, the user is redirected to the Menu Page.

> - As a first-time user, I want to see an attractive logo when I open the app. So that I can easily recognize and remember the app.
> - As a first-times user, I would like a personalized feel of my name being used inside the application.

![Landing Page](assets/readme_images/welcome_page.png)

#### Menu Page:

##### Objective: 

Provide navigational choices to the user for exploring different features of the application.

##### Design Elements:

- Logo: Continuity is maintained with the logo positioned at the top of the page.
- Personalized Greeting: A "Hello" message that includes the user's name (if provided) to reinforce personalization.
- Menu Options: Clearly numbered options guide the user to their next activity:<br>
Enter 1 to know your traits.<br>
Enter 2 to know your daily horoscope.<br>
Enter 3 to exit.<br>

##### User Flow:

- User is greeted by name (if provided) and sees the menu options.
- User selects an option by entering the corresponding number.
- The application directs the user to the appropriate page based on their selection.

> - As a first-times user, I would like a simple and clear options to enhance usability and reduce confusion.

![Menu Page](assets/readme_images/main_menu.png)

#### Zodiac Signs Page: 

##### Objective: 

Assist users in identifying their zodiac sign based on their birth date.

##### Design Elements:

- List of Zodiac Signs: Each zodiac sign is listed alongside its corresponding date range in brackets, aiding users who are unfamiliar with zodiac periods.
- Instructional Prompt: Users are guided on how to select their zodiac sign, enhancing usability.

##### User Flow:

- User is presented with a list of zodiac signs and corresponding date ranges.
- User identifies and selects their zodiac sign based on their birth date.
- Depending on their previous menu selection:
  - If option 1 was selected, the user is directed to a page detailing the traits of their chosen zodiac sign.
  - If option 2 was selected, the user is directed to a page where the user has to select for which day they want to know thier horoscope.

> - As a first-time user, I want to be able to determine my zodiac sign based on my month of birth. So that I can engage with content that is relevant to me without prior knowledge of astrology. 
> - As a first-time user, I want to choose my zodiac sign from a list. So that I can see specific insights related to my sign.
> - As a frequent user, I want the process of selecting zodiac signs and fetching results to be quick and simple. So that I can enjoy a seamless experience without unnecessary delays.

![Zodiac Signs](assets/readme_images/zodiac_signs_list.png)


#### Zodiac's Traits Result Page:

##### Objective: 

Display detailed traits of the selected zodiac sign in an engaging and visually appealing format.

##### Design Elements:

- Zodiac Symbol Image: Prominently displays an artistic or symbolic representation of the chosen zodiac sign at the top of the page. This visual serves not only as an attractive feature but also helps reinforce the identity of the sign.
- Zodiac Name: The name of the zodiac sign is displayed next to the image, serving as a clear identifier and header for the information that follows.
- Traits List: Traits of the zodiac sign are presented in a list format. The traits begin with the starting letter of the zodiac's name, adding a creative and thematic touch to the content presentation.
- Colorful Design: The page uses colors that are associated with or complement the zodiac sign, enhancing visual engagement and making the information more appealing.
- Navigation Options: At the bottom of the page, users are provided with options to navigate back to the menu or exit the application. The options are clearly labeled "Enter Y to return to the menu" and "Enter N to exit the game."

##### User Flow:

- After selecting their zodiac sign on the previous page, the user is directed to the Zodiac Traits Result Page.
- The user is greeted by an image of their zodiac symbol alongside the name of the sign, immediately confirming their choice.
- Below the header, the user can read a list of traits that start with the same letter as the zodiac sign, making the information easy to follow and engaging.
- The user can take their time to read through the traits, which are designed to be both informative and enjoyable.
- After reviewing the traits, users find navigation options at the bottom of the page, allowing them to choose their next action.

> - As a first-time user, I want the app to be colorful, have images, animations and engaging. So that my experience learning about my zodiac traits is fun and visually appealing.
> - As a first-time user, I want easy options to navigate back or exit the app. So that I can have a smooth user experience without feeling stuck in any part of the app.
> - As a frequent user, I want the process of selecting zodiac signs and fetching results to be quick and simple. So that I can enjoy a seamless experience without unnecessary delays.

![Zodiac Traits Result](assets/readme_images/zodiac_traits_result.png)

#### Day Page: 

##### Objective: 

Provide users with the ability to select a specific day for which they want to view their horoscope, enhancing the personalization of their experience.

##### Design Elements:

- Day Options: Clearly listed options for "yesterday," "today," and "tomorrow" allow users to choose the specific day for which they wish to receive a horoscope. This provides flexibility and relevance to the user’s daily life.
- Prompt for Input: Below the list of days, there is a clear prompt asking the user to enter the number corresponding to their chosen day. This ensures the interaction is straightforward and minimizes confusion.

##### User Flow:

- Upon choosing to view their horoscope (option 2 on the Menu Page), and selecting their zodiac sign, users are directed to the Day List Page.
- Users see a list of days—yesterday, today, tomorrow—each assigned a number (1, 2, 3).
- Users are prompted to enter the number for the day they are interested in.
- After inputting their choice, users are directed to the Horoscope Result Page where they can view the horoscope for the selected day.

> As a first-time user, I want to choose the day for which I want to know my horoscope. So that I can get insights for specific days, past, present or future.

![Day List Page](assets/readme_images/day_list.png)

#### Daily Horoscope Result Page: 

##### Objective: 

Display a personalized horoscope for the user based on their zodiac sign and the selected day, ensuring fresh and relevant content is delivered by fetching daily updates from a reliable source.

##### Design Elements:

- Zodiac and Day Information: At the top of the page, the user's chosen zodiac sign and the selected day (yesterday, today, tomorrow) are prominently displayed. This helps reinforce the personalization of the information and sets context for the horoscope result.
- Horoscope Content: Directly below the zodiac and day information, the horoscope result is displayed. This content is updated daily from the horoscope.com website to ensure it is timely and relevant.
- Colorful Design: The page uses colors that complement the result, enhancing visual engagement and making the information more appealing.
- Navigation Options: At the bottom of the page, users are given options to either return to the menu by pressing "Y" or to exit the application by pressing "N". This offers straightforward navigation tailored to the user's preference for continued use or closing the session.
- Unlimited Access: Users can check their horoscope multiple times for multiple zodiac signs without any restrictions, enhancing the utility and flexibility of the application.

#### User Flow:

- After selecting their zodiac sign and the day for which they want the horoscope on the Day List Page, users are directed here.
- Users are greeted with the name of their zodiac and the day they have chosen, providing clear confirmation of their selections.
- The personalized horoscope, fetched from horoscope.com, is displayed, offering insights based on astrological predictions for the selected day.
- After reviewing their horoscope, users decide whether to return to the main menu for more activities or to exit the application.

> - As a first-time user, I want easy options to navigate back or exit the app. So that I can have a smooth user experience without feeling stuck in any part of the app.
> - As a first-time user, I want the app to be colorful, have images, animations and engaging. So that my experience learning about my zodiac traits is fun and visually appealing.
> - As a frequent user, I want the horoscopes to be updated daily. So that I can rely on the app for fresh and relevant astrological insights every day.
> - As a frequent user, I want to check not only my horoscope but also those of my friends and family without restrictions. So that I can share and discuss these insights with them.
> - As a frequent user, I want the process of selecting zodiac signs and fetching results to be quick and simple. So that I can enjoy a seamless experience without unnecessary delays.

![Daily Horoscope Result](assets/readme_images/horoscope_result.png)

#### Thank You Page:

##### Objective: 

Provide a pleasant and friendly closure to the user's session in the application, confirming their successful exit and offering guidance on how to re-engage with the app if desired.

##### Design Elements:

- Colorful Owl Image: A charming and colorful illustration of an owl is prominently displayed on this page. The owl can symbolize wisdom and is often well-received in visual communications, making it a fitting choice for conveying a thoughtful goodbye.
- Thank You Message: Positioned directly below the owl, this message thanks the user for using the application, enhancing the personal touch and expressing appreciation for the user’s time and interaction.
- Re-engagement Instruction: A small message at the bottom of the page instructs users on how to restart the application by clicking the "Run Program" button. This provides clear guidance for users who might want to use the app again, making re-engagement straightforward.

##### User Flow:

- When the user selects the option to exit at any page where this choice is provided, they are directed to the Thank You Page.
- The user is greeted by the visually appealing owl image, along with a thank you message acknowledging their use of the app.
- At the end of the session, the user reads the note on how to restart the application, offering a clear path to return if they choose.

> - As a first time user, I would like to see some confirmation if I have successfully exited out of the application.


![Thank You](assets/readme_images/thank_you_page.png)

#### Loading Animation Page:

##### Objective: 
Provide an engaging and visually appealing experience during data processing times, reducing perceived wait times and keeping the user entertained.

##### Design Elements:

- Animated Zodiac Symbols: A dynamic animation featuring zodiac symbols transitioning from one to another, representing all twelve zodiac signs. This animation not only keeps the user visually engaged but also reinforces the astrological theme of the application.
- Loading Message: Positioned directly below the animation, a clear message such as "Loading your results..." informs the user that their request is being processed. This communication helps manage user expectations during the wait.
- Application Logo: Displayed at the top of the page, the application logo maintains brand presence and continuity throughout the user experience, anchoring the page visually.

##### User Flow:

- After the user inputs their choices for either zodiac traits or their daily horoscope, they are directed to the Loading Animation Page.
- As the backend processes the request, users see a captivating display of zodiac symbols transitioning smoothly, which keeps them entertained.
- The loading message reassures them that their results are on the way, reducing potential frustration associated with waiting.
- Once the data processing is complete, the user is automatically redirected to the respective result page (Zodiac Traits Result Page or Horoscope Result Page).

> - As a first-time user, I want to see an attractive logo when I open the app. So that I can easily recognize and remember the app.
> - As a frequent user, I want to see some animations while waiting for results. So that the waiting time is more enjoyable and the app feels lively.

![Loading Animation](assets/readme_images/loading_animation.gif)

#### Typing Animation:

##### Objective: 
Enhance the visual appeal and engagement of textual content by using a typing animation effect, making the display of text more dynamic and engaging.

##### Design Elements:

- Typing Animation: The application employs a typing animation where text appears character by character, simulating the effect of someone typing the text in real time. This animation is used primarily for displaying key information to the user, adding an element of interactivity and visual interest.

##### User Flow:

- Whenever text needs to be displayed prompting for user input, the typing animation begins.
- The user watches as the text gradually appears on the screen, enhancing their reading experience and maintaining their attention.
- Once the animation completes, the text remains on the screen for the user to read at their leisure and give their input.

> - As a first-time user, I want the app to be colorful, have images, animations and engaging. So that my experience learning about my zodiac traits is fun and visually appealing.

![Typing Animation](assets/readme_images/typing_animation.gif)

#### Error Messages:

##### Objective: 

Provide clear, immediate feedback when user input is invalid or outside the expected range, guiding them to correct their entries effectively.

##### Design Elements:

- Color-Coded Messages: Error messages are displayed in red, a common color that is universally understood to denote warnings or errors. This helps to immediately draw the user's attention to the issue.
- Specific Instructions: The error message specifies exactly what the user needs to do to correct their input, such as "Please Enter a number between 1 to 3" or "Please Enter a number between 1 to 12." This specificity helps prevent user frustration and guides them towards successful interaction.

##### User Flow:

- The user enters a response when prompted by the application.
- If the input is invalid—such as being out of the expected numerical range, empty, an alphabet, or containing symbols—an error message in red is displayed.
- The user reads the error message, understands the mistake, and is guided to re-enter a valid input based on the provided instructions.

> - As a first time user I would like clear instructions and feedback to rectify if I make any mistake.

![Error Message 1](assets/readme_images/error_1.png)
![Error Message 2](assets/readme_images/error_2.png)
![Error Message 3](assets/readme_images/error_3.png)


<!-- ### Future Features:
##### Sound Effects: 
Implementing sound effects to enhance the gaming experience, making it more enjoyable and immersive for users.

##### Difficulty Modes: 
Introducing easy and hard modes to cater to varying skill levels and preferences among players. This allows users to adjust the game's difficulty according to their proficiency and desired level of challenge.

##### Guess Distribution Graph: 
Adding a graphical representation of guess distribution in the statistics section, similar to the original Wordle version. This feature provides insights into the user's guessing patterns and performance over time.

##### Login Feature: 
Incorporating a login feature to enable users to save their game statistics and progress to their account. This allows users to access their data from different devices and continue their gameplay seamlessly.

##### Expanded Theme Selection: 
Adding more themes with vibrant colors and diverse designs to enhance the visual appeal of the gameplay. Offering a variety of themes allows users to customize their gaming experience according to their preferences and mood.

## Testing:
##### Browser Compatibility:
  - Tested playing the game in Chrome, Firefox, and Safari browsers.
  - Confirmed that the game functions smoothly across different browsers without any issues.
##### Responsive Design:
  - Played the game on various devices including mobile phones, laptops, and desktop computers.
  - Ensured that the game is responsive and adapts well to different screen sizes.
#### Accessibility:
  - Ran Lighthouse tests to evaluate the accessibility of the website.
  - Verified that the website has a high accessibility rating, ensuring inclusivity for all users.
##### Gameplay Features:
  - Tested all the features of the gameplay, including entering guesses, resetting the game, and changing themes.
  - Confirmed that the gameplay mechanics work as expected without any errors.
##### Theme Compatibility:
  - Played the game multiple times with different themes to ensure compatibility.
  - Verified that the gameplay flows smoothly with all theme options without encountering any issues.
##### Modal and Menu Functionality:
  - Verified that modals and menus open and close properly when clicking the respective icons.
  - Ensured that all modal content and menu options are displayed correctly.
##### Animations and Alert Messages:
  - Confirmed that animations, alert messages, and tile colors change appropriately during gameplay interactions.
##### Game Controls:
  - Tested the functionality of the reset button, mode toggle button, and keyboard keys.
  - Ensured that the page reloads when clicking the reset button and toggles between light and dark modes when clicking the mode button.
  - Verified that all keyboard keys function correctly and change colors according to tile statuses.
##### Theme Consistency:
  - Checked that the color of the tiles and background of the "How to Play" modal change accordingly based on the selected theme.
  - Confirmed that theme changes are reflected consistently throughout the gameplay interface.
##### Statistics Update:
  - Checked that the statistics are updated accurately in the statistics menu after each gameplay session.
  - Verified that statistics such as win percentage are displayed correctly and reflect the user's progress.
##### Conclusion:
  - Overall, the testing confirms that Wordle functions smoothly, providing an enjoyable, colorful and error-free gaming experience across different browsers, devices, and themes.

### Validator Testing:
- HTML files pass through the [W3C validator](https://validator.w3.org/) with no issues found.

   - Result for index.html
   ![index.html](documentation/html-validator.png)

- CSS files pass through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/) with no issues found.

   - Result for CSS.
   ![CSS](documentation/css-validator.png)

- The Javascript files passed through the [Javascript validator](https://jshint.com/) testing.

   - Result for Javascript.
   ![Javascript](documentation/javascript-validator.png)

- All pages has a good Accessibility rating in Lighthouse.

   - Result for Lighthouse testing.
      ##### Light Mode:
      ![Light Mode Lighthouse](documentation/lighthouse-lightmode.png)

      ##### Dark Mode:
      ![Dark Mode Lighthouse](documentation/lighthouse-darkmode.png)

### Bugs:
##### Tile Color Change Bug: 
Initially, the tiles were not changing colors after flipping when different themes were set. Upon investigation, it was discovered that the respective color theme classes were not added to the tiles in the CSS. Adding these classes resolved the issue.

##### Overlay Effect Disappearance: 
The overlay effect applied to the "How to Play" and "Statistics" modals disappeared when clicking anywhere inside the modals. Assigning different overlay classes to each modal solved this problem, ensuring the overlay effect remained intact.

##### Close Button Dysfunctionality: 
On smaller screens, the close button in the "How to Play" modal was not functioning properly. Increasing the z-index of the modal resolved this issue, allowing users to close the modal seamlessly.

##### Unintended Modal Opening: 
While the themes menu was open, users could click on other icons and open additional modals without closing the themes menu. To address this bug, a transparent overlay was created to block access to other icons when the themes menu is open, ensuring proper behavior.

##### Theme and Mode Reset Bug: 
Themes and modes were reverting to default settings upon page reset. Implementing local storage to save theme and mode selections ensured that these preferences persisted across page resets.

##### Flash of White Background: 
When the reset icon was pressed in dark mode, there was a brief flash of white background. This issue was debugged by moving the theme reset code to the top of the HTML, eliminating the flash of white background upon reset.

These bug fixes and debugging efforts contribute to a smoother and more seamless user experience, ensuring that the game functions as intended across different scenarios and interactions.

### Unfixed Bugs:
- There is no unfixed bugs to my knowledge.

## Technologies Used
### Main Languages Used:
- HTML5
- CSS3
- Javascript

### Frameworks, Libraries & Programs Used:
- Font Awesome - To add icons to the nav bar and close button in themes menu and statistics modal.
- GitPod - To create my html files, stylesheet and javascript before pushing the project to Github.
- GitHub - To store my repository for submission.
- Figma - To create wireframe for project.
- Coolors - To pick color for the website.
- Vistaprint - To create logo for the website.
- Am I responsive - To see the responsiveness of the screen.

## Deployment
1. In the GitHub repositories, navigate your way to the settings tab
2. From there on your left hand side find the 'Pages' tab, click on it.
3. In the build and deployment section, select 'source' and then 'deploy from a branch'
4. Then underneath that select 'main' and 'root' 
5. Click save
6. Your page should refresh automatically or manually with a link to your deployed website. 
7. The link can be found here: [Wordle](https://yagavi1994.github.io/Wordle/)

### How to Fork:
- Log in (or sign up) to [Github](https://github.com/).
- Go to respository for this project [Wordle](https://github.com/Yagavi1994/Wordle).
- Click the fork button in the top right corner.

### How to Clone:
- Log in (or sign up) to [Github](https://github.com/).
- Go to respository for this project [Wordle](https://github.com/Yagavi1994/Wordle).
- Click on the code button, select whether you would like to clone with HTTPS, SSH, GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the clone directory.
- Type 'git clone' into terminal and then paste the link you copied in step 3.
- Press enter.

## Credits
- I would like to credit the [Wordle](https://www.nytimes.com/games/wordle/index.html) game, which served as inspiration for this project. Wordle has been a favorite pastime for me, and its gameplay mechanics influenced the development of this project.
- I extend my gratitude to my mentor, Martina Terlevic, for her invaluable guidance and support throughout the project. Her encouragement and feedback played a significant role in shaping the project and boosting my confidence.
- Special thanks to my husband, who is a game designer, for his constructive criticism and attention to detail in the UI and UX aspects of the project. His insights greatly contributed to the refinement of the project.
- I would like to credit my cousin who is a developer, for his assistance in resolving some JavaScript bugs and adding the confetti animation to the game.
- I appreciate the valuable inputs provided by a fellow student  Dajana Isbaner in the peer code review. 

#### Code
- I would like to credit [Web Dev Simplified](https://www.youtube.com/watch?v=Wak7iN4JZzU) for their helpful tutorial, which provided guidance and assistance in writing the code for the main function of the game.
 -->
