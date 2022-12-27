#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    // Check if a search query was provided as an argument
    if (argc < 2) {
        printf("Error: No search query provided\n");
        return 1;
    }

    // Concatenate the search query into a string
    char search_query[256];
    for (int i = 1; i < argc; i++) {
        strcat(search_query, argv[i]);
        strcat(search_query, " ");
    }

    // Build the command to open the default browser with the search query
    char command[256];
    sprintf(command, "xdg-open 'https://www.google.com/search?q=%s'", search_query);

    // Execute the command using system()
    int result = system(command);

    // Check the result of the command
    if (result != 0) {
        printf("Error: Failed to open default browser\n");
        return 1;
    }

    return 0;
}
