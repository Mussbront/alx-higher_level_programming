#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - check if a lincked list contains a cycle
  * @list: The linked list to check
  *Return: 1 if the list contains a cycle. 0 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list)
	{
		while (list != NULL)
		{
			current = list;
			list = list->next;
			if (current <= list)
				return (1);
		}
		return (0);
	}
	return (0);

}
