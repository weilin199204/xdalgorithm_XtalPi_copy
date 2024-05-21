class CLICommand(object):

    """Interface for a CLI command.

    This class represents a top level CLI command

    """

    @property
    def name(self):
        # Subclasses must implement a name.
        raise NotImplementedError("name")

    @name.setter
    def name(self, value):
        # Subclasses must implement setting/changing the cmd name.
        raise NotImplementedError("name")

    @property
    def lineage(self):
        # Represents how to get to a specific command using the CLI.
        # It includes all commands that came before it and itself in
        # a list.
        return [self]

    @property
    def lineage_names(self):
        # Represents the lineage of a command in terms of command ``name``
        return [cmd.name for cmd in self.lineage]

    def __call__(self, args, parsed_globals):
        """Invoke CLI operation.

        :type args: str
        :param args: The remaining command line args.

        :type parsed_globals: ``argparse.Namespace``
        :param parsed_globals: The parsed arguments so far.

        :rtype: int
        :return: The return code of the operation.  This will be used
            as the RC code for the ``aws`` process.

        """
        # Subclasses are expected to implement this method.
        pass

    def create_help_command(self):
        # Subclasses are expected to implement this method if they want
        # help docs.
        return None

    @property
    def arg_table(self):
        return {}
