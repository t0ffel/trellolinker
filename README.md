# trellolinker

## Configuration structure

`parent_lists` - declares the lists of parent cards
`child_boards` - declares the boards of child cards

## Relations

Parent(Project) card will have checklists.
Checklists(OKR) will have checklist line items.
Checklist line items(KR) correspond to child cards.

## Actions

### Populate checklists

List child cards corresponding to a parent.
Detect separate checklists, split child cards into groups.
Record status of child cards, shortlink to child cards.
Repopulate parent card: delete old checklists, create new checklists.

