# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gen.amizone_pb2 as amizone__pb2


class AmizoneServiceStub(object):
    """@todo authentication service for JWT tokens as secure alternative to BasicAuth."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAttendance = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetAttendance",
            request_serializer=amizone__pb2.EmptyMessage.SerializeToString,
            response_deserializer=amizone__pb2.AttendanceRecords.FromString,
        )
        self.GetClassSchedule = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetClassSchedule",
            request_serializer=amizone__pb2.ClassScheduleRequest.SerializeToString,
            response_deserializer=amizone__pb2.ScheduledClasses.FromString,
        )
        self.GetExamSchedule = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetExamSchedule",
            request_serializer=amizone__pb2.EmptyMessage.SerializeToString,
            response_deserializer=amizone__pb2.ExaminationSchedule.FromString,
        )
        self.GetSemesters = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetSemesters",
            request_serializer=amizone__pb2.EmptyMessage.SerializeToString,
            response_deserializer=amizone__pb2.SemesterList.FromString,
        )
        self.GetCourses = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetCourses",
            request_serializer=amizone__pb2.SemesterRef.SerializeToString,
            response_deserializer=amizone__pb2.Courses.FromString,
        )
        self.GetCurrentCourses = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetCurrentCourses",
            request_serializer=amizone__pb2.EmptyMessage.SerializeToString,
            response_deserializer=amizone__pb2.Courses.FromString,
        )
        self.GetExamResult = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetExamResult",
            request_serializer=amizone__pb2.SemesterRef.SerializeToString,
            response_deserializer=amizone__pb2.ExamResultRecords.FromString,
        )
        self.GetCurrentExamResult = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetCurrentExamResult",
            request_serializer=amizone__pb2.EmptyMessage.SerializeToString,
            response_deserializer=amizone__pb2.ExamResultRecords.FromString,
        )
        self.GetUserProfile = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetUserProfile",
            request_serializer=amizone__pb2.EmptyMessage.SerializeToString,
            response_deserializer=amizone__pb2.Profile.FromString,
        )
        self.GetWifiMacInfo = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/GetWifiMacInfo",
            request_serializer=amizone__pb2.EmptyMessage.SerializeToString,
            response_deserializer=amizone__pb2.WifiMacInfo.FromString,
        )
        self.RegisterWifiMac = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/RegisterWifiMac",
            request_serializer=amizone__pb2.RegisterWifiMacRequest.SerializeToString,
            response_deserializer=amizone__pb2.EmptyMessage.FromString,
        )
        self.DeregisterWifiMac = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/DeregisterWifiMac",
            request_serializer=amizone__pb2.DeregisterWifiMacRequest.SerializeToString,
            response_deserializer=amizone__pb2.EmptyMessage.FromString,
        )
        self.FillFacultyFeedback = channel.unary_unary(
            "/go_amizone.server.proto.v1.AmizoneService/FillFacultyFeedback",
            request_serializer=amizone__pb2.FillFacultyFeedbackRequest.SerializeToString,
            response_deserializer=amizone__pb2.FillFacultyFeedbackResponse.FromString,
        )


class AmizoneServiceServicer(object):
    """@todo authentication service for JWT tokens as secure alternative to BasicAuth."""

    def GetAttendance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetClassSchedule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExamSchedule(self, request, context):
        """GetExamSchedule returns exam schedule. Amizone only allows access to schedules for the ongoing semester
        and only close to the exam dates, so we don't take any parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetSemesters(self, request, context):
        """GetSemesters returns a list of semesters that include past semesters and the current semester.
        These semesters can be used in other RPCs that consume them, for example GetCourses.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCourses(self, request, context):
        """GetCourses returns a list of courses for the given semester."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCurrentCourses(self, request, context):
        """GetCurrentCourses returns a list of courses for the "current" semester."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExamResult(self, request, context):
        """GetExamResult returns the exam result for the given semester."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCurrentExamResult(self, request, context):
        """GetCurrentExamResult returns the exam result for the "current" semester."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUserProfile(self, request, context):
        """GetUserProfile returns the user's profile."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetWifiMacInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RegisterWifiMac(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeregisterWifiMac(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FillFacultyFeedback(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AmizoneServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetAttendance": grpc.unary_unary_rpc_method_handler(
            servicer.GetAttendance,
            request_deserializer=amizone__pb2.EmptyMessage.FromString,
            response_serializer=amizone__pb2.AttendanceRecords.SerializeToString,
        ),
        "GetClassSchedule": grpc.unary_unary_rpc_method_handler(
            servicer.GetClassSchedule,
            request_deserializer=amizone__pb2.ClassScheduleRequest.FromString,
            response_serializer=amizone__pb2.ScheduledClasses.SerializeToString,
        ),
        "GetExamSchedule": grpc.unary_unary_rpc_method_handler(
            servicer.GetExamSchedule,
            request_deserializer=amizone__pb2.EmptyMessage.FromString,
            response_serializer=amizone__pb2.ExaminationSchedule.SerializeToString,
        ),
        "GetSemesters": grpc.unary_unary_rpc_method_handler(
            servicer.GetSemesters,
            request_deserializer=amizone__pb2.EmptyMessage.FromString,
            response_serializer=amizone__pb2.SemesterList.SerializeToString,
        ),
        "GetCourses": grpc.unary_unary_rpc_method_handler(
            servicer.GetCourses,
            request_deserializer=amizone__pb2.SemesterRef.FromString,
            response_serializer=amizone__pb2.Courses.SerializeToString,
        ),
        "GetCurrentCourses": grpc.unary_unary_rpc_method_handler(
            servicer.GetCurrentCourses,
            request_deserializer=amizone__pb2.EmptyMessage.FromString,
            response_serializer=amizone__pb2.Courses.SerializeToString,
        ),
        "GetExamResult": grpc.unary_unary_rpc_method_handler(
            servicer.GetExamResult,
            request_deserializer=amizone__pb2.SemesterRef.FromString,
            response_serializer=amizone__pb2.ExamResultRecords.SerializeToString,
        ),
        "GetCurrentExamResult": grpc.unary_unary_rpc_method_handler(
            servicer.GetCurrentExamResult,
            request_deserializer=amizone__pb2.EmptyMessage.FromString,
            response_serializer=amizone__pb2.ExamResultRecords.SerializeToString,
        ),
        "GetUserProfile": grpc.unary_unary_rpc_method_handler(
            servicer.GetUserProfile,
            request_deserializer=amizone__pb2.EmptyMessage.FromString,
            response_serializer=amizone__pb2.Profile.SerializeToString,
        ),
        "GetWifiMacInfo": grpc.unary_unary_rpc_method_handler(
            servicer.GetWifiMacInfo,
            request_deserializer=amizone__pb2.EmptyMessage.FromString,
            response_serializer=amizone__pb2.WifiMacInfo.SerializeToString,
        ),
        "RegisterWifiMac": grpc.unary_unary_rpc_method_handler(
            servicer.RegisterWifiMac,
            request_deserializer=amizone__pb2.RegisterWifiMacRequest.FromString,
            response_serializer=amizone__pb2.EmptyMessage.SerializeToString,
        ),
        "DeregisterWifiMac": grpc.unary_unary_rpc_method_handler(
            servicer.DeregisterWifiMac,
            request_deserializer=amizone__pb2.DeregisterWifiMacRequest.FromString,
            response_serializer=amizone__pb2.EmptyMessage.SerializeToString,
        ),
        "FillFacultyFeedback": grpc.unary_unary_rpc_method_handler(
            servicer.FillFacultyFeedback,
            request_deserializer=amizone__pb2.FillFacultyFeedbackRequest.FromString,
            response_serializer=amizone__pb2.FillFacultyFeedbackResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "go_amizone.server.proto.v1.AmizoneService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class AmizoneService(object):
    """@todo authentication service for JWT tokens as secure alternative to BasicAuth."""

    @staticmethod
    def GetAttendance(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetAttendance",
            amizone__pb2.EmptyMessage.SerializeToString,
            amizone__pb2.AttendanceRecords.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetClassSchedule(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetClassSchedule",
            amizone__pb2.ClassScheduleRequest.SerializeToString,
            amizone__pb2.ScheduledClasses.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetExamSchedule(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetExamSchedule",
            amizone__pb2.EmptyMessage.SerializeToString,
            amizone__pb2.ExaminationSchedule.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetSemesters(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetSemesters",
            amizone__pb2.EmptyMessage.SerializeToString,
            amizone__pb2.SemesterList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetCourses(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetCourses",
            amizone__pb2.SemesterRef.SerializeToString,
            amizone__pb2.Courses.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetCurrentCourses(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetCurrentCourses",
            amizone__pb2.EmptyMessage.SerializeToString,
            amizone__pb2.Courses.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetExamResult(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetExamResult",
            amizone__pb2.SemesterRef.SerializeToString,
            amizone__pb2.ExamResultRecords.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetCurrentExamResult(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetCurrentExamResult",
            amizone__pb2.EmptyMessage.SerializeToString,
            amizone__pb2.ExamResultRecords.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetUserProfile(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetUserProfile",
            amizone__pb2.EmptyMessage.SerializeToString,
            amizone__pb2.Profile.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetWifiMacInfo(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/GetWifiMacInfo",
            amizone__pb2.EmptyMessage.SerializeToString,
            amizone__pb2.WifiMacInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RegisterWifiMac(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/RegisterWifiMac",
            amizone__pb2.RegisterWifiMacRequest.SerializeToString,
            amizone__pb2.EmptyMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeregisterWifiMac(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/DeregisterWifiMac",
            amizone__pb2.DeregisterWifiMacRequest.SerializeToString,
            amizone__pb2.EmptyMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def FillFacultyFeedback(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/go_amizone.server.proto.v1.AmizoneService/FillFacultyFeedback",
            amizone__pb2.FillFacultyFeedbackRequest.SerializeToString,
            amizone__pb2.FillFacultyFeedbackResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
