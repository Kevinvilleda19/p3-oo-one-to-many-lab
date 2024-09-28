class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types are {Pet.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Default to no owner initially

        if owner is not None:
            # Validate that owner is an instance of Owner
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class")
            self.set_owner(owner)

        # Add the current instance to the class-level 'all' list
        Pet.all.append(self)

    def set_owner(self, owner):
        """Assign an owner to the pet and add the pet to the owner's pet list"""
        self.owner = owner
        owner.add_pet(self)

    def __repr__(self):
        return f"Pet(name='{self.name}', pet_type='{self.pet_type}', owner='{self.owner.name if self.owner else 'None'}')"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        # Return the full list of the owner's pets
        return self._pets

    def add_pet(self, pet):
        # Validate that pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of the Pet class")

        # Assign the current owner to the pet and add the pet to the owner's pet list
        if pet not in self._pets:  # Prevent duplicate additions
            pet.owner = self
            self._pets.append(pet)

    def get_sorted_pets(self):
        # Return a sorted list of the owner's pets by their names
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name='{self.name}')"
