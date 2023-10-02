# Metaphor API Mini-Project

This is a mini-project I made using the metaphor.ai API. It is a very basic Python file that takes in a text file that the user has generated, and for each line uses the Metaphor search endpoint to find the most relevant link and then parses that link to output a bibliography of the sentences written. This could be expanded to include a UI component for more popular text editors, or to have real-time parsing of the lines written in a dialog box.


To run this project, generate your own Metaphor API key and replace `METAPHOR_API_KEY` to run the project. Feel free to change the test input. Make sure that the first line of the test input is either the string "apa" or "mla", with or without proper case. This tells the program whether to output the bibliographical results in APA or MLA citation format.
