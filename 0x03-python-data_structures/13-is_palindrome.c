#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current_node;
	char buf[10000];
	int i, length = 0;

	if (!*head || !head)
		return (1);

	current_node = *head;
	if (!current_node->next)
		return (1);

	while (current_node)
	{
		buf[length] = current_node->n;
		current_node = current_node->next;
		length++;
	}
	length = length - 1;
	for (; length >= 0 && i <= length; length--, i++)
	{
		if (buf[length] != buf[i])
			return (0);
	}
	return (1);
}
