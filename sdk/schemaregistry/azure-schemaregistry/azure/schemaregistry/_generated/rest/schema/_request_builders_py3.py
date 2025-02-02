# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, IO, Optional, TypeVar

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _format_url_section
T = TypeVar('T')
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_by_id_request(
    id: str,
    **kwargs: Any
) -> HttpRequest:
    """Get a registered schema by its unique ID reference.

    Gets a registered schema by its unique ID.  Azure Schema Registry guarantees that ID is unique
    within a namespace. Operation response type is based on serialization of schema requested.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param id: References specific schema in registry namespace.
    :type id: str
    :keyword api_version: Api Version. The default value is "2021-10". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop('api_version', "2021-10")  # type: str

    accept = "application/json; serialization=Avro"
    # Construct URL
    url = kwargs.pop("template_url", '/$schemaGroups/$schemas/{id}')
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_versions_request(
    group_name: str,
    schema_name: str,
    **kwargs: Any
) -> HttpRequest:
    """Get list schema versions.

    Gets the list of all versions of one schema.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param group_name: Schema group under which schema is registered.  Group's serialization type
     should match the serialization type specified in the request.
    :type group_name: str
    :param schema_name: Name of schema being registered.
    :type schema_name: str
    :keyword api_version: Api Version. The default value is "2021-10". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "schemaVersions": [
                    0  # Optional. Array of schema groups.
                ]
            }
    """

    api_version = kwargs.pop('api_version', "2021-10")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/$schemaGroups/{groupName}/schemas/{schemaName}/versions')
    path_format_arguments = {
        "groupName": _SERIALIZER.url("group_name", group_name, 'str'),
        "schemaName": _SERIALIZER.url("schema_name", schema_name, 'str', max_length=50, min_length=0, pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_query_id_by_content_request(
    group_name: str,
    schema_name: str,
    *,
    content: Any,
    **kwargs: Any
) -> HttpRequest:
    """Get ID for existing schema.

    Gets the ID referencing an existing schema within the specified schema group, as matched by
    schema content comparison.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param group_name: Schema group under which schema is registered.  Group's serialization type
     should match the serialization type specified in the request.
    :type group_name: str
    :param schema_name: Name of requested schema.
    :type schema_name: str
    :keyword api_version: Api Version. The default value is "2021-10". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). String representation (UTF-8) of the registered schema.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop('api_version', "2021-10")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/$schemaGroups/{groupName}/schemas/{schemaName}:get-id')
    path_format_arguments = {
        "groupName": _SERIALIZER.url("group_name", group_name, 'str'),
        "schemaName": _SERIALIZER.url("schema_name", schema_name, 'str', max_length=50, min_length=0, pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        content=content,
        **kwargs
    )


def build_register_request(
    group_name: str,
    schema_name: str,
    *,
    content: Any,
    **kwargs: Any
) -> HttpRequest:
    """Register new schema.

    Register new schema. If schema of specified name does not exist in specified group, schema is
    created at version 1. If schema of specified name exists already in specified group, schema is
    created at latest version + 1.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param group_name: Schema group under which schema should be registered.  Group's serialization
     type should match the serialization type specified in the request.
    :type group_name: str
    :param schema_name: Name of schema being registered.
    :type schema_name: str
    :keyword api_version: Api Version. The default value is "2021-10". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). String representation (UTF-8) of the schema being
     registered.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop('api_version', "2021-10")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/$schemaGroups/{groupName}/schemas/{schemaName}')
    path_format_arguments = {
        "groupName": _SERIALIZER.url("group_name", group_name, 'str'),
        "schemaName": _SERIALIZER.url("schema_name", schema_name, 'str', max_length=50, min_length=0, pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        content=content,
        **kwargs
    )

