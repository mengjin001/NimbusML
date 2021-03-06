# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
"""
Roles definition.
"""


class RoleError(ValueError):
    """
    Raised when a role is mispelled.
    """

    def __init__(self, role, allowed=None):
        if allowed is None:
            allowed = DataRoles._allowed
        allowed = list(sorted(allowed))
        msg = "Unknown role '{0}'. Available: {1}".format(role, allowed)
        ValueError.__init__(self, msg)


class Role:
    """

    Some columns play a specific role for specific learners or transforms.
    This is the complete list.

    .. remarks::
        Column roles can be specified for each transform and learner during
        initialization.
        For more details, please refer to
        `Roles </nimbusml/concepts/roles#roles-and-learners>`_.

    Example:
        .. code-block:: python

            from nimbusml import Role
            from nimbusml import Pipeline  # similar to Pipeline
            from nimbusml.linear_model import FastLinearRegressor
            import pandas
            X = pandas.DataFrame(dict(education=[2,4,6,4,3],
                                        workclass=[0,2,3,4,0],
                                        weights=[1., 1., 1., 2., 1.],
                                        y=[1.1, 2.2, 1.24, 3.4, 3.4]))
            lr = FastLinearRegressor() \
                << {Role.Label:'y', Role.Feature:['weights', 'workclass']}

            # equivalent to
            # FastLinearRegressor(label = 'y',
                                  feature = ['weights', 'workclass'])

            exp = Pipeline([lr])
            exp.fit(X)
            prediction = exp.predict(X)

    """

    Feature = 'Feature'
    Label = 'Label'
    Weight = 'Weight'
    GroupId = 'GroupId'
    User = 'User'
    Item = 'Item'
    Name = 'Name'
    RowId = 'RowId'

    @staticmethod
    def to_attribute(role, suffix="_column"):
        """
        Converts a role into an attribute name.
        ``GroupId --> group_id_column``.
        """
        if not isinstance(role, str):
            raise TypeError("Unexpected role '{0}'".format(role))
        if role == "GroupId":
            return "group_id" + suffix
        if role == "RowId":
            return "row_id" + suffix
        return role.lower() + suffix


class DataRoles(Role):
    """
    Defines roles for a schema.
    """

    # REVIEW: this list needs to be updated every time a new learner
    # invents a new role.
    # Maybe every learner and transform could declare the roles it requires to
    # train and predict.
    _allowed = set(
        k for k in Role.__dict__ if k[0] != '_' and k[0].upper() == k[0])
    _allowed_attr = {Role.to_attribute(k): Role.to_attribute(
        k, suffix='') for k in Role.__dict__ if
        k[0] != '_' and k[0].upper() == k[0]}

    @staticmethod
    def check_role(role):
        """
        Checks that role is allowed.
        """
        if role not in DataRoles._allowed:
            raise RoleError(role)

    def __init__(self, roles=None):
        """
        :param roles: roles definition as a dictionary

        Roles defines how columns are used if not overwritten
        by a trainer or a transform. Roles can be
        label, feature, group, weight.
        """
        if roles is not None:
            if not isinstance(roles, dict):
                raise TypeError(
                    "roles must be a dictionary (not {0}).".format(
                        type(roles)))

        self._roles = roles
        self._verify_roles()

    def clone(self):
        return DataRoles(self._roles.copy() if self._roles else None)

    def _verify_roles(self, schema=None):
        """
        Checks that a role belongs to the schema.
        """
        if self._roles is not None:
            for k, v in self._roles.items():
                if k not in DataRoles._allowed:
                    raise ValueError("Role '{0}' is not allowed.".format(k))
                if schema is not None:
                    if k not in schema:
                        raise RuntimeError(
                            "Column '{0}' not in schema '{1}'".format(
                                k, schema))

    @property
    def Roles(self):
        return self._roles

    def __len__(self):
        return len(self._roles) if self._roles is not None else 0

    def __str__(self):
        return str(self._roles) if self._roles is not None else ''

    def _set_role(self, role_name, column_name):
        """
        Defines a role for a column.
        """
        if self._roles is None:
            self._roles = {}
        self._roles[role_name] = column_name
        self._verify_roles()

    def _get_role(self, role_name):
        """
        Returns the column associated to a role.
        """
        if self._roles is None:
            raise RuntimeError("No role is defined.")
        if role_name not in self._roles:
            raise ValueError("Role '{0}' is not defined.".format(role_name))
        return self._roles[role_name]

    def _has_role(self, role_name):
        """
        Tells if a particular role is defined.
        """
        if self._roles is None:
            return False
        return role_name in self._roles

    def __eq__(self, other):
        """
        Checks roles are equal.
        """
        return self._roles == other._roles

    def items(self):
        """
        Returns an iterator on roles.
        """
        return self._roles.items()
