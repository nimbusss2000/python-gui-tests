
def test_del_group(app):
    old_list = app.groups.get_group_list()
    # some_group = app.groups.choose_some_group()
    some_group = app.groups.choose_first_group()
    app.groups.delete_group(some_group)
    new_list = app.groups.get_group_list()
    old_list = old_list[1:]
    assert sorted(old_list) == sorted(new_list)