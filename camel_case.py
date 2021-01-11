def to_camel_case(text):
    is_lower = False
    if text.split('-')[0][0].islower():
        is_lower = True
    if is_lower:
        word = ''.join(word.title() for word in text.split('-'))
        return word[0].upper()


print(to_camel_case('the-stealTH-warrior'))



###############################################################################
# test.describe("Testing function to_camel_case")
# test.it("Basic tests")
# test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")