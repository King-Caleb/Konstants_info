# Konstants/API.py
print("""
🎉🎉 Welcome to the **Konstants Community 1.0.0**! 🎉🎉
We're thrilled to have you on board! 🚀
⚡ Start by creating your first constant, and let the fun begin! ⚡
""")

"""
This module provides a way to create immutable constants and group them together in a way that prevents modification.
The constants are stored in special classes that ensure the values cannot be altered once set, providing a mechanism
for safe, constant values.

The module includes the following key components:

1. **Const class**:
   - Represents an immutable constant value.
   - Prevents any attempt to modify the value after it has been set.
   - Only strings and numbers are allowed as constant values.
   - Other types, like lists and dictionaries, are automatically converted into immutable forms (tuples and frozen sets).
   - The `get()` method allows access to the value of the constant.

2. **Group class**:
   - A container for multiple constants.
   - Allows you to group related constants together, making it easier to manage them.
   - Constants are stored as attributes within the Group.
   - The group can be displayed with or without the "Group()" wrapper around its contents.
   - The `__repr__` method controls the string representation of the group, showing either the "Group()" wrapper or just the constants, depending on the `show_group` flag.

3. **Helper Functions**:
   - `create(value)`: A utility function to create a constant (`Const`) object. If the value is a list or dictionary, it's converted to an immutable form (tuple or frozen set).
   - `create_group(**constants)`: Creates a `Group` of constants, automatically wrapping non-constant values in `Const` objects.
   - `PrintG(group)`: Prints the contents of a `Group` object. The output can be customized to hide or show the "Group()" wrapper based on the `show_group` flag in the `Group` class.

4. **Operations on Constants**:
   - The module includes basic arithmetic operations (addition, subtraction, multiplication, and division) for `Const` objects:
     - `addK`, `subK`, `multK`, and `divK` allow arithmetic between `Const` objects and return a new `Const` object with the result.

Usage Example:
--------------
# Create individual constants
A = Const("A", 100)
B = Const("B", [1, 2, 3])

# Group constants together
group1 = create_group(A=A, B=B, C={'key1': 'value1', 'key2': 'value2'})

# Print group with or without the "Group()" wrapper
PrintG(group1)

# Perform arithmetic on constants
result = addK(A, B, "A_plus_B")
print(result.get())  # Output will be 100 + (1, 2, 3)

"""


class Const:
    def __init__(self, name, value, is_creation=False):
        self._is_creation = is_creation
        self._value = value
        object.__setattr__(self, "_name", name)
        object.__setattr__(self, "_value", value)
        object.__setattr__(self, "_is_creation", is_creation)

    def __setattr__(self, name, value):
        # Only allow modification of _value during creation (via create function)
        if name == "_value" and not self._is_creation:
            raise AttributeError(f"Cannot modify constant: {name}")
        else:
            # Allow any other attribute modification (e.g., _name, _is_creation)
            super().__setattr__(name, value)

    def get(self):
        return self._value


class Group:
    def __init__(self, show_group=True, **constants):
        """Initialize a constant Group with optional constants."""
        self.show_group = show_group  # Boolean to control whether to show 'Group()'
        self._constants = {}

        # Initialize with the provided constants
        for name, value in constants.items():
            self.add_constant(name, value)

    def add_constant(self, name, value):
        """Add a new constant to the namespace."""
        # If it's not already a Const object, wrap it in one
        if not isinstance(value, Const):
            value = create(value)

        # Add the constant to the dictionary
        self._constants[name] = value

    def __getattr__(self, name):
        """Access constants as attributes."""
        if name in self._constants:
            return self._constants[name]
        raise AttributeError(f"Constant '{name}' not found.")

    def __repr__(self):
        """Return a cleaner string representation of all constants in the constant Group."""
        if self.show_group:
            # Show the full Group() form
            return f"Group({', '.join(f'{name}: {const.get()}' for name, const in self._constants.items())})"
        else:
            # Show only constants, no Group() wrapper
            return ', '.join(f"{name}: {const.get()}" for name, const in self._constants.items())

    def __sub__(self, other):
        """Toggle the show_group flag when the - operator is used."""
        if not isinstance(other, Group):
            raise TypeError("The '-' operator can only be used with another Group object.")

        # Toggle the show_group value
        self.show_group = not self.show_group
        return self  # Return the modified group


def PrintG(group):
    a = group.__repr__()
    # Remove the "Group(" part from the beginning
    z = a.replace("Group(", ")")
    # Remove the ")" part from the end
    dis = z.replace(")", "")
    print(dis)


def create_group(**constants):
    """Helper function to create a group of constants."""
    for name, value in constants.items():
        if not isinstance(value, Const):
            constants[name] = create(value)  # Convert non-const values to Const
    return Group(**constants)  # Return a constant Group


def Kprint(const_obj):
    """Prints the value of a Const object."""
    if isinstance(const_obj, Const):
        print(const_obj.get())
    else:
        raise TypeError("Kprint expects a Const object.")


def create(value):
    """Create a Const object (used to modify the value)."""
    # If it's a list, convert to tuple, if dict, convert to frozenset
    if isinstance(value, list):
        return Const("Constant", tuple(value), is_creation=True)
    elif isinstance(value, dict):
        return Const("Constant", frozenset(value.items()), is_creation=True)
    else:
        return Const("Constant", value, is_creation=True)


def addK(const1, const2, new_name):
    """Add two constants and return a new Const object."""
    if not isinstance(const1, Const) or not isinstance(const2, Const):
        raise TypeError("Both arguments must be Const objects.")

    result_value = const1.get() + const2.get()
    return Const(new_name, result_value)


def subK(const1, const2, new_name):
    """Subtract two constants and return a new Const object."""
    if not isinstance(const1, Const) or not isinstance(const2, Const):
        raise TypeError("Both arguments must be Const objects.")

    result_value = const1.get() - const2.get()
    return Const(new_name, result_value)


def divK(const1, const2, new_name):
    """Divide two constants and return a new Const object."""
    if not isinstance(const1, Const) or not isinstance(const2, Const):
        raise TypeError("Both arguments must be Const objects.")

    # Handle division by zero
    if const2.get() == 0:
        raise ValueError("Cannot divide by zero.")

    result_value = const1.get() / const2.get()
    return Const(new_name, result_value)


def multK(const1, const2, new_name):
    """Multiply two constants and return a new Const object."""
    if not isinstance(const1, Const) or not isinstance(const2, Const):
        raise TypeError("Both arguments must be Const objects.")

    result_value = const1.get() * const2.get()
    return Const(new_name, result_value)
