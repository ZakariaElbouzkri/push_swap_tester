#include<stdio.h>
#include<readline/readline.h>

int main(int ac, char **av)
{
	char *line;

	line = readline("");
	while (line)
	{
		printf("%s", line);
	}

}