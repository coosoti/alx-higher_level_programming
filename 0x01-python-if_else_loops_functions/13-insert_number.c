#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: the head of the linked list
 * @number: data in the new node
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *first;

	first = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || first->n > newnode->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (first->next != NULL)
	{
		if ((first->next->n > newnode->n && first->n < newnode->n)
			|| newnode->n == first->n)
		{
			newnode->next = first->next;
			first->next = newnode;
			return (newnode);
		}
		first = first->next;
	}
	newnode->next = first->next;
	first->next = newnode;
	return (newnode);
}
