# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pmesh')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pmesh')
    _pmesh = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pmesh', [dirname(__file__)])
        except ImportError:
            import _pmesh
            return _pmesh
        try:
            _mod = imp.load_module('_pmesh', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pmesh = swig_import_helper()
    del swig_import_helper
else:
    import _pmesh
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


MFEM_VERSION = _pmesh.MFEM_VERSION
MFEM_VERSION_STRING = _pmesh.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _pmesh.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _pmesh.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _pmesh.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _pmesh.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _pmesh.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _pmesh.MFEM_VERSION_PATCH
MFEM_TIMER_TYPE = _pmesh.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _pmesh.MFEM_HYPRE_VERSION
import mfem._par.mesh
import mfem._par.matrix
import mfem._par.vector
import mfem._par.array
import mfem._par.ostream_typemap
import mfem._par.operators
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.densemat
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.coefficient
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.handle
import mfem._par.hypre
import mfem._par.bilininteg
import mfem._par.linearform
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
class ParMesh(mfem._par.mesh.Mesh):
    """Proxy of C++ mfem::ParMesh class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.mesh.Mesh]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParMesh, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.mesh.Mesh]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParMesh, name)
    __repr__ = _swig_repr

    def GetComm(self):
        """GetComm(ParMesh self) -> MPI_Comm"""
        return _pmesh.ParMesh_GetComm(self)


    def GetNRanks(self):
        """GetNRanks(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNRanks(self)


    def GetMyRank(self):
        """GetMyRank(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetMyRank(self)

    __swig_getmethods__["gtopo"] = _pmesh.ParMesh_gtopo_get
    if _newclass:
        gtopo = _swig_property(_pmesh.ParMesh_gtopo_get)
    __swig_setmethods__["have_face_nbr_data"] = _pmesh.ParMesh_have_face_nbr_data_set
    __swig_getmethods__["have_face_nbr_data"] = _pmesh.ParMesh_have_face_nbr_data_get
    if _newclass:
        have_face_nbr_data = _swig_property(_pmesh.ParMesh_have_face_nbr_data_get, _pmesh.ParMesh_have_face_nbr_data_set)
    __swig_setmethods__["face_nbr_group"] = _pmesh.ParMesh_face_nbr_group_set
    __swig_getmethods__["face_nbr_group"] = _pmesh.ParMesh_face_nbr_group_get
    if _newclass:
        face_nbr_group = _swig_property(_pmesh.ParMesh_face_nbr_group_get, _pmesh.ParMesh_face_nbr_group_set)
    __swig_setmethods__["face_nbr_elements_offset"] = _pmesh.ParMesh_face_nbr_elements_offset_set
    __swig_getmethods__["face_nbr_elements_offset"] = _pmesh.ParMesh_face_nbr_elements_offset_get
    if _newclass:
        face_nbr_elements_offset = _swig_property(_pmesh.ParMesh_face_nbr_elements_offset_get, _pmesh.ParMesh_face_nbr_elements_offset_set)
    __swig_setmethods__["face_nbr_vertices_offset"] = _pmesh.ParMesh_face_nbr_vertices_offset_set
    __swig_getmethods__["face_nbr_vertices_offset"] = _pmesh.ParMesh_face_nbr_vertices_offset_get
    if _newclass:
        face_nbr_vertices_offset = _swig_property(_pmesh.ParMesh_face_nbr_vertices_offset_get, _pmesh.ParMesh_face_nbr_vertices_offset_set)
    __swig_getmethods__["face_nbr_elements"] = _pmesh.ParMesh_face_nbr_elements_get
    if _newclass:
        face_nbr_elements = _swig_property(_pmesh.ParMesh_face_nbr_elements_get)
    __swig_getmethods__["face_nbr_vertices"] = _pmesh.ParMesh_face_nbr_vertices_get
    if _newclass:
        face_nbr_vertices = _swig_property(_pmesh.ParMesh_face_nbr_vertices_get)
    __swig_setmethods__["send_face_nbr_elements"] = _pmesh.ParMesh_send_face_nbr_elements_set
    __swig_getmethods__["send_face_nbr_elements"] = _pmesh.ParMesh_send_face_nbr_elements_get
    if _newclass:
        send_face_nbr_elements = _swig_property(_pmesh.ParMesh_send_face_nbr_elements_get, _pmesh.ParMesh_send_face_nbr_elements_set)
    __swig_setmethods__["send_face_nbr_vertices"] = _pmesh.ParMesh_send_face_nbr_vertices_set
    __swig_getmethods__["send_face_nbr_vertices"] = _pmesh.ParMesh_send_face_nbr_vertices_get
    if _newclass:
        send_face_nbr_vertices = _swig_property(_pmesh.ParMesh_send_face_nbr_vertices_get, _pmesh.ParMesh_send_face_nbr_vertices_set)
    __swig_setmethods__["pncmesh"] = _pmesh.ParMesh_pncmesh_set
    __swig_getmethods__["pncmesh"] = _pmesh.ParMesh_pncmesh_get
    if _newclass:
        pncmesh = _swig_property(_pmesh.ParMesh_pncmesh_get, _pmesh.ParMesh_pncmesh_set)

    def GetNGroups(self):
        """GetNGroups(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNGroups(self)


    def GroupNVertices(self, group):
        """GroupNVertices(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNVertices(self, group)


    def GroupNEdges(self, group):
        """GroupNEdges(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNEdges(self, group)


    def GroupNFaces(self, group):
        """GroupNFaces(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNFaces(self, group)


    def GroupVertex(self, group, i):
        """GroupVertex(ParMesh self, int group, int i) -> int"""
        return _pmesh.ParMesh_GroupVertex(self, group, i)


    def GroupEdge(self, group, i, *args):
        if len(args) == 0:
            from mfem.par import intp  
            edge = intp()
            o = intp()  
            _pmesh.ParMesh_GroupEdge(self, group, i, edge, o)
            return edge.value(), o.value()
        else:
            return _pmesh.ParMesh_GroupEdge(self, group, i, *args)      



    def GroupFace(self, group, i, *args):
        if len(args) == 0:
            from mfem.par import intp    
            face = intp()
            o = intp()
            _pmesh.Mesh_ParGroupFace(self, group, i, face, o)      
            return face.value(), o.value()
        else:
            return _pmesh.ParMesh_GroupFace(self, group, i, *args)            



    def GenerateOffsets(self, N, loc_sizes, offsets):
        """GenerateOffsets(ParMesh self, int N, HYPRE_Int [] loc_sizes, mfem::Array< HYPRE_Int > *[] offsets)"""
        return _pmesh.ParMesh_GenerateOffsets(self, N, loc_sizes, offsets)


    def ExchangeFaceNbrData(self):
        """ExchangeFaceNbrData(ParMesh self)"""
        return _pmesh.ParMesh_ExchangeFaceNbrData(self)


    def ExchangeFaceNbrNodes(self):
        """ExchangeFaceNbrNodes(ParMesh self)"""
        return _pmesh.ParMesh_ExchangeFaceNbrNodes(self)


    def GetNFaceNeighbors(self):
        """GetNFaceNeighbors(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNFaceNeighbors(self)


    def GetFaceNbrGroup(self, fn):
        """GetFaceNbrGroup(ParMesh self, int fn) -> int"""
        return _pmesh.ParMesh_GetFaceNbrGroup(self, fn)


    def GetFaceNbrRank(self, fn):
        """GetFaceNbrRank(ParMesh self, int fn) -> int"""
        return _pmesh.ParMesh_GetFaceNbrRank(self, fn)


    def GetFaceToAllElementTable(self):
        """GetFaceToAllElementTable(ParMesh self) -> Table"""
        return _pmesh.ParMesh_GetFaceToAllElementTable(self)


    def GetSharedFaceTransformations(self, sf, fill2=True):
        """
        GetSharedFaceTransformations(ParMesh self, int sf, bool fill2=True) -> FaceElementTransformations
        GetSharedFaceTransformations(ParMesh self, int sf) -> FaceElementTransformations
        """
        return _pmesh.ParMesh_GetSharedFaceTransformations(self, sf, fill2)


    def GetNSharedFaces(self):
        """GetNSharedFaces(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNSharedFaces(self)


    def GetSharedFace(self, sface):
        """GetSharedFace(ParMesh self, int sface) -> int"""
        return _pmesh.ParMesh_GetSharedFace(self, sface)


    def ReorientTetMesh(self):
        """ReorientTetMesh(ParMesh self)"""
        return _pmesh.ParMesh_ReorientTetMesh(self)


    def ReduceInt(self, value):
        """ReduceInt(ParMesh self, int value) -> long"""
        return _pmesh.ParMesh_ReduceInt(self, value)


    def RefineGroups(self, v_to_v, middle):
        """RefineGroups(ParMesh self, DSTable v_to_v, int * middle)"""
        return _pmesh.ParMesh_RefineGroups(self, v_to_v, middle)


    def Rebalance(self):
        """Rebalance(ParMesh self)"""
        return _pmesh.ParMesh_Rebalance(self)


    def Print(self, *args):
        """
        Print(ParMesh self, std::ostream & out)
        Print(ParMesh self)
        """
        return _pmesh.ParMesh_Print(self, *args)


    def PrintXG(self, *args):
        """
        PrintXG(ParMesh self, std::ostream & out)
        PrintXG(ParMesh self)
        """
        return _pmesh.ParMesh_PrintXG(self, *args)


    def PrintAsOne(self, *args):
        """
        PrintAsOne(ParMesh self, std::ostream & out)
        PrintAsOne(ParMesh self)
        """
        return _pmesh.ParMesh_PrintAsOne(self, *args)


    def PrintAsOneXG(self, *args):
        """
        PrintAsOneXG(ParMesh self, std::ostream & out)
        PrintAsOneXG(ParMesh self)
        """
        return _pmesh.ParMesh_PrintAsOneXG(self, *args)


    def GetBoundingBox(self, ref = 2):
        from  .vector import Vector
        min = Vector()
        max = Vector()      
        _mesh.Mesh_GetBoundingBox(self, min, max, ref)      
        return min.GetDataArray().copy(), max.GetDataArray().copy()



    def GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max):
        """GetCharacteristics(ParMesh self, double & h_min, double & h_max, double & kappa_min, double & kappa_max)"""
        return _pmesh.ParMesh_GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max)


    def PrintInfo(self, *args):
        """
        PrintInfo(ParMesh self, std::ostream & out)
        PrintInfo(ParMesh self)
        """
        return _pmesh.ParMesh_PrintInfo(self, *args)


    def ParPrint(self, out):
        """ParPrint(ParMesh self, std::ostream & out)"""
        return _pmesh.ParMesh_ParPrint(self, out)


    def FindPoints(self, point_mat, elem_ids, ips, warn=True, inv_trans=None):
        """
        FindPoints(ParMesh self, DenseMatrix point_mat, intArray elem_ids, IntegrationPointArray ips, bool warn=True, InverseElementTransformation inv_trans=None) -> int
        FindPoints(ParMesh self, DenseMatrix point_mat, intArray elem_ids, IntegrationPointArray ips, bool warn=True) -> int
        FindPoints(ParMesh self, DenseMatrix point_mat, intArray elem_ids, IntegrationPointArray ips) -> int
        """
        return _pmesh.ParMesh_FindPoints(self, point_mat, elem_ids, ips, warn, inv_trans)

    __swig_destroy__ = _pmesh.delete_ParMesh
    __del__ = lambda self: None

    def __init__(self, *args):
        """
        __init__(mfem::ParMesh self, ParMesh pmesh, bool copy_nodes=True) -> ParMesh
        __init__(mfem::ParMesh self, ParMesh pmesh) -> ParMesh
        __init__(mfem::ParMesh self, MPI_Comm comm, Mesh mesh, int * partitioning_=None, int part_method=1) -> ParMesh
        __init__(mfem::ParMesh self, MPI_Comm comm, Mesh mesh, int * partitioning_=None) -> ParMesh
        __init__(mfem::ParMesh self, MPI_Comm comm, Mesh mesh) -> ParMesh
        __init__(mfem::ParMesh self, MPI_Comm comm, std::istream & input) -> ParMesh
        __init__(mfem::ParMesh self, ParMesh orig_mesh, int ref_factor, int ref_type) -> ParMesh
        __init__(mfem::ParMesh self, MPI_Comm comm, char const * mesh_file) -> ParMesh
        """
        this = _pmesh.new_ParMesh(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def ParPrintToFile(self, mesh_file, precision):
        """ParPrintToFile(ParMesh self, char const * mesh_file, int const precision)"""
        return _pmesh.ParMesh_ParPrintToFile(self, mesh_file, precision)

ParMesh_swigregister = _pmesh.ParMesh_swigregister
ParMesh_swigregister(ParMesh)

# This file is compatible with both classic and new-style classes.


