| Specification                                                                                                   | Test Case Id | Purpose                                                                                 |
|-----------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------|
| The name of the ticket has to be alphanumeric-only, space allowed only if it is not the first or last character | R5.1.1       | Make sure that no other requests grant the user information they are not suppose to see |
| Name of ticket no longer than 60 Character                                                                      | R5.1.2       | The character limit is 60, 60 characters is enough                                      |
| Quantity of the ticket has to be more than 0 and less than equal to 100.                                        | R5.2         | Cant have more then 100 tickets                                                         |
| Ticket quantity can not be zero                                                                                 | R5.3.1       | Make sure that the user has at least 1 ticket for quantity                              |
| Ticket quantity can not be greater then 100                                                                     | R5.3.2       | Make sure users are limited to 100 tickets so other users can buy them to               |
| Price range [10,100]                                                                                            | R5.4.1       | Check if price is under 10                                                              |
| Price range [10,100]                                                                                            | R5.4.2       | Check if price is over 100                                                              |
| Data must be given in the format YYYYMMDD                                                                       | R5.5         | Keeps the formatting consistent                                                         |
| Ticket of the given name must exist                                                                             | R5.6         | Ticket must exist firs to be updated                                                    |
| For any errors, redirect back to/ and show an error message                                                     | R5.7         | All Errors show message to as why for ease of use for user.                             |