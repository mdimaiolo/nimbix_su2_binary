# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""'pysu2ad' module"""


from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pysu2ad')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pysu2ad')
    _pysu2ad = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pysu2ad', [dirname(__file__)])
        except ImportError:
            import _pysu2ad
            return _pysu2ad
        try:
            _mod = imp.load_module('_pysu2ad', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pysu2ad = swig_import_helper()
    del swig_import_helper
else:
    import _pysu2ad
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


class SwigPyIterator(_object):
    """Proxy of C++ swig::SwigPyIterator class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pysu2ad.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        """value(SwigPyIterator self) -> PyObject *"""
        return _pysu2ad.SwigPyIterator_value(self)


    def incr(self, n=1):
        """
        incr(SwigPyIterator self, size_t n=1) -> SwigPyIterator
        incr(SwigPyIterator self) -> SwigPyIterator
        """
        return _pysu2ad.SwigPyIterator_incr(self, n)


    def decr(self, n=1):
        """
        decr(SwigPyIterator self, size_t n=1) -> SwigPyIterator
        decr(SwigPyIterator self) -> SwigPyIterator
        """
        return _pysu2ad.SwigPyIterator_decr(self, n)


    def distance(self, x):
        """distance(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t"""
        return _pysu2ad.SwigPyIterator_distance(self, x)


    def equal(self, x):
        """equal(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _pysu2ad.SwigPyIterator_equal(self, x)


    def copy(self):
        """copy(SwigPyIterator self) -> SwigPyIterator"""
        return _pysu2ad.SwigPyIterator_copy(self)


    def next(self):
        """next(SwigPyIterator self) -> PyObject *"""
        return _pysu2ad.SwigPyIterator_next(self)


    def __next__(self):
        """__next__(SwigPyIterator self) -> PyObject *"""
        return _pysu2ad.SwigPyIterator___next__(self)


    def previous(self):
        """previous(SwigPyIterator self) -> PyObject *"""
        return _pysu2ad.SwigPyIterator_previous(self)


    def advance(self, n):
        """advance(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2ad.SwigPyIterator_advance(self, n)


    def __eq__(self, x):
        """__eq__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _pysu2ad.SwigPyIterator___eq__(self, x)


    def __ne__(self, x):
        """__ne__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _pysu2ad.SwigPyIterator___ne__(self, x)


    def __iadd__(self, n):
        """__iadd__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2ad.SwigPyIterator___iadd__(self, n)


    def __isub__(self, n):
        """__isub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2ad.SwigPyIterator___isub__(self, n)


    def __add__(self, n):
        """__add__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2ad.SwigPyIterator___add__(self, n)


    def __sub__(self, *args):
        """
        __sub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator
        __sub__(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t
        """
        return _pysu2ad.SwigPyIterator___sub__(self, *args)

    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pysu2ad.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SU2_CFD = _pysu2ad.SU2_CFD
SU2_DEF = _pysu2ad.SU2_DEF
SU2_DOT = _pysu2ad.SU2_DOT
SU2_GEO = _pysu2ad.SU2_GEO
SU2_SOL = _pysu2ad.SU2_SOL
class CDriver(_object):
    """Proxy of C++ CDriver class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CDriver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CDriver, name)
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator, dummy_geo):
        """__init__(CDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator, bool dummy_geo) -> CDriver"""
        this = _pysu2ad.new_CDriver(confFile, val_nZone, MPICommunicator, dummy_geo)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pysu2ad.delete_CDriver
    __del__ = lambda self: None

    def Run(self):
        """Run(CDriver self)"""
        return _pysu2ad.CDriver_Run(self)


    def StartSolver(self):
        """StartSolver(CDriver self)"""
        return _pysu2ad.CDriver_StartSolver(self)


    def Postprocessing(self):
        """Postprocessing(CDriver self)"""
        return _pysu2ad.CDriver_Postprocessing(self)


    def ResetConvergence(self):
        """ResetConvergence(CDriver self)"""
        return _pysu2ad.CDriver_ResetConvergence(self)


    def Preprocess(self, TimeIter):
        """Preprocess(CDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CDriver_Preprocess(self, TimeIter)


    def Monitor(self, TimeIter):
        """Monitor(CDriver self, unsigned long TimeIter) -> bool"""
        return _pysu2ad.CDriver_Monitor(self, TimeIter)


    def Output(self, TimeIter):
        """Output(CDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CDriver_Output(self, TimeIter)


    def DynamicMeshUpdate(self, *args):
        """
        DynamicMeshUpdate(CDriver self, unsigned long TimeIter)
        DynamicMeshUpdate(CDriver self, unsigned short val_iZone, unsigned long TimeIter)
        """
        return _pysu2ad.CDriver_DynamicMeshUpdate(self, *args)


    def SetInitialMesh(self):
        """SetInitialMesh(CDriver self)"""
        return _pysu2ad.CDriver_SetInitialMesh(self)


    def BoundaryConditionsUpdate(self):
        """BoundaryConditionsUpdate(CDriver self)"""
        return _pysu2ad.CDriver_BoundaryConditionsUpdate(self)


    def Get_Drag(self):
        """Get_Drag(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_Get_Drag(self)


    def Get_Lift(self):
        """Get_Lift(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_Get_Lift(self)


    def Get_Mx(self):
        """Get_Mx(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_Get_Mx(self)


    def Get_My(self):
        """Get_My(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_Get_My(self)


    def Get_Mz(self):
        """Get_Mz(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_Get_Mz(self)


    def Get_DragCoeff(self):
        """Get_DragCoeff(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_Get_DragCoeff(self)


    def Get_LiftCoeff(self):
        """Get_LiftCoeff(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_Get_LiftCoeff(self)


    def GetNumberVertices(self, iMarker):
        """GetNumberVertices(CDriver self, unsigned short iMarker) -> unsigned long"""
        return _pysu2ad.CDriver_GetNumberVertices(self, iMarker)


    def GetNumberHaloVertices(self, iMarker):
        """GetNumberHaloVertices(CDriver self, unsigned short iMarker) -> unsigned long"""
        return _pysu2ad.CDriver_GetNumberHaloVertices(self, iMarker)


    def IsAHaloNode(self, iMarker, iVertex):
        """IsAHaloNode(CDriver self, unsigned short iMarker, unsigned long iVertex) -> bool"""
        return _pysu2ad.CDriver_IsAHaloNode(self, iMarker, iVertex)


    def GetnTimeIter(self):
        """GetnTimeIter(CDriver self) -> unsigned long"""
        return _pysu2ad.CDriver_GetnTimeIter(self)


    def GetTime_Iter(self):
        """GetTime_Iter(CDriver self) -> unsigned long"""
        return _pysu2ad.CDriver_GetTime_Iter(self)


    def GetUnsteady_TimeStep(self):
        """GetUnsteady_TimeStep(CDriver self) -> passivedouble"""
        return _pysu2ad.CDriver_GetUnsteady_TimeStep(self)


    def GetVertexGlobalIndex(self, iMarker, iVertex):
        """GetVertexGlobalIndex(CDriver self, unsigned short iMarker, unsigned long iVertex) -> unsigned long"""
        return _pysu2ad.CDriver_GetVertexGlobalIndex(self, iMarker, iVertex)


    def GetInitialMeshCoord(self, iMarker, iVertex):
        """GetInitialMeshCoord(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetInitialMeshCoord(self, iMarker, iVertex)


    def GetVertexTemperature(self, iMarker, iVertex):
        """GetVertexTemperature(CDriver self, unsigned short iMarker, unsigned long iVertex) -> passivedouble"""
        return _pysu2ad.CDriver_GetVertexTemperature(self, iMarker, iVertex)


    def SetVertexTemperature(self, iMarker, iVertex, val_WallTemp):
        """SetVertexTemperature(CDriver self, unsigned short iMarker, unsigned long iVertex, passivedouble val_WallTemp)"""
        return _pysu2ad.CDriver_SetVertexTemperature(self, iMarker, iVertex, val_WallTemp)


    def GetVertexHeatFluxes(self, iMarker, iVertex):
        """GetVertexHeatFluxes(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetVertexHeatFluxes(self, iMarker, iVertex)


    def GetVertexNormalHeatFlux(self, iMarker, iVertex):
        """GetVertexNormalHeatFlux(CDriver self, unsigned short iMarker, unsigned long iVertex) -> passivedouble"""
        return _pysu2ad.CDriver_GetVertexNormalHeatFlux(self, iMarker, iVertex)


    def SetVertexNormalHeatFlux(self, iMarker, iVertex, val_WallHeatFlux):
        """SetVertexNormalHeatFlux(CDriver self, unsigned short iMarker, unsigned long iVertex, passivedouble val_WallHeatFlux)"""
        return _pysu2ad.CDriver_SetVertexNormalHeatFlux(self, iMarker, iVertex, val_WallHeatFlux)


    def GetThermalConductivity(self, iMarker, iVertex):
        """GetThermalConductivity(CDriver self, unsigned short iMarker, unsigned long iVertex) -> passivedouble"""
        return _pysu2ad.CDriver_GetThermalConductivity(self, iMarker, iVertex)


    def Inlet_Preprocessing(self, solver, geometry, config):
        """Inlet_Preprocessing(CDriver self, CSolver *** solver, CGeometry ** geometry, CConfig * config)"""
        return _pysu2ad.CDriver_Inlet_Preprocessing(self, solver, geometry, config)


    def GetVertexUnitNormal(self, iMarker, iVertex):
        """GetVertexUnitNormal(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetVertexUnitNormal(self, iMarker, iVertex)


    def GetAllBoundaryMarkersTag(self):
        """GetAllBoundaryMarkersTag(CDriver self) -> std::vector< std::string >"""
        return _pysu2ad.CDriver_GetAllBoundaryMarkersTag(self)


    def GetAllDeformMeshMarkersTag(self):
        """GetAllDeformMeshMarkersTag(CDriver self) -> std::vector< std::string >"""
        return _pysu2ad.CDriver_GetAllDeformMeshMarkersTag(self)


    def GetAllCHTMarkersTag(self):
        """GetAllCHTMarkersTag(CDriver self) -> std::vector< std::string >"""
        return _pysu2ad.CDriver_GetAllCHTMarkersTag(self)


    def GetAllInletMarkersTag(self):
        """GetAllInletMarkersTag(CDriver self) -> std::vector< std::string >"""
        return _pysu2ad.CDriver_GetAllInletMarkersTag(self)


    def GetAllBoundaryMarkers(self):
        """GetAllBoundaryMarkers(CDriver self) -> std::map< std::string,int >"""
        return _pysu2ad.CDriver_GetAllBoundaryMarkers(self)


    def GetAllBoundaryMarkersType(self):
        """GetAllBoundaryMarkersType(CDriver self) -> std::map< std::string,std::string >"""
        return _pysu2ad.CDriver_GetAllBoundaryMarkersType(self)


    def SetMeshDisplacement(self, iMarker, iVertex, DispX, DispY, DispZ):
        """SetMeshDisplacement(CDriver self, unsigned short iMarker, unsigned long iVertex, passivedouble DispX, passivedouble DispY, passivedouble DispZ)"""
        return _pysu2ad.CDriver_SetMeshDisplacement(self, iMarker, iVertex, DispX, DispY, DispZ)


    def CommunicateMeshDisplacement(self):
        """CommunicateMeshDisplacement(CDriver self)"""
        return _pysu2ad.CDriver_CommunicateMeshDisplacement(self)


    def GetMeshDisp_Sensitivity(self, iMarker, iVertex):
        """GetMeshDisp_Sensitivity(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetMeshDisp_Sensitivity(self, iMarker, iVertex)


    def SetFEA_Loads(self, iMarker, iVertex, LoadX, LoadY, LoadZ):
        """SetFEA_Loads(CDriver self, unsigned short iMarker, unsigned long iVertex, passivedouble LoadX, passivedouble LoadY, passivedouble LoadZ)"""
        return _pysu2ad.CDriver_SetFEA_Loads(self, iMarker, iVertex, LoadX, LoadY, LoadZ)


    def GetFEA_Displacements(self, iMarker, iVertex):
        """GetFEA_Displacements(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetFEA_Displacements(self, iMarker, iVertex)


    def GetFEA_Velocity(self, iMarker, iVertex):
        """GetFEA_Velocity(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetFEA_Velocity(self, iMarker, iVertex)


    def GetFEA_Velocity_n(self, iMarker, iVertex):
        """GetFEA_Velocity_n(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetFEA_Velocity_n(self, iMarker, iVertex)


    def GetFlowLoad_Sensitivity(self, iMarker, iVertex):
        """GetFlowLoad_Sensitivity(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetFlowLoad_Sensitivity(self, iMarker, iVertex)


    def GetFlowLoad(self, iMarker, iVertex):
        """GetFlowLoad(CDriver self, unsigned short iMarker, unsigned long iVertex) -> std::vector< passivedouble >"""
        return _pysu2ad.CDriver_GetFlowLoad(self, iMarker, iVertex)


    def SetFlowLoad_Adjoint(self, iMarker, iVertex, val_AdjointX, val_AdjointY, val_AdjointZ):
        """SetFlowLoad_Adjoint(CDriver self, unsigned short iMarker, unsigned long iVertex, passivedouble val_AdjointX, passivedouble val_AdjointY, passivedouble val_AdjointZ)"""
        return _pysu2ad.CDriver_SetFlowLoad_Adjoint(self, iMarker, iVertex, val_AdjointX, val_AdjointY, val_AdjointZ)


    def SetSourceTerm_DispAdjoint(self, iMarker, iVertex, val_AdjointX, val_AdjointY, val_AdjointZ):
        """SetSourceTerm_DispAdjoint(CDriver self, unsigned short iMarker, unsigned long iVertex, passivedouble val_AdjointX, passivedouble val_AdjointY, passivedouble val_AdjointZ)"""
        return _pysu2ad.CDriver_SetSourceTerm_DispAdjoint(self, iMarker, iVertex, val_AdjointX, val_AdjointY, val_AdjointZ)


    def SetHeatSource_Position(self, alpha, pos_x, pos_y, pos_z):
        """SetHeatSource_Position(CDriver self, passivedouble alpha, passivedouble pos_x, passivedouble pos_y, passivedouble pos_z)"""
        return _pysu2ad.CDriver_SetHeatSource_Position(self, alpha, pos_x, pos_y, pos_z)


    def SetInlet_Angle(self, iMarker, alpha):
        """SetInlet_Angle(CDriver self, unsigned short iMarker, passivedouble alpha)"""
        return _pysu2ad.CDriver_SetInlet_Angle(self, iMarker, alpha)


    def GetTotalNumberOfVariables(self, iZone, adjoint):
        """GetTotalNumberOfVariables(CDriver self, unsigned short iZone, bool adjoint) -> unsigned short"""
        return _pysu2ad.CDriver_GetTotalNumberOfVariables(self, iZone, adjoint)

CDriver_swigregister = _pysu2ad.CDriver_swigregister
CDriver_swigregister(CDriver)
cvar = _pysu2ad.cvar
MESH_0 = cvar.MESH_0
MESH_1 = cvar.MESH_1
ZONE_0 = cvar.ZONE_0
ZONE_1 = cvar.ZONE_1

class CFluidDriver(CDriver):
    """Proxy of C++ CFluidDriver class."""

    __swig_setmethods__ = {}
    for _s in [CDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CFluidDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [CDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CFluidDriver, name)
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        """__init__(CFluidDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CFluidDriver"""
        this = _pysu2ad.new_CFluidDriver(confFile, val_nZone, MPICommunicator)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pysu2ad.delete_CFluidDriver
    __del__ = lambda self: None

    def StartSolver(self):
        """StartSolver(CFluidDriver self)"""
        return _pysu2ad.CFluidDriver_StartSolver(self)


    def Run(self):
        """Run(CFluidDriver self)"""
        return _pysu2ad.CFluidDriver_Run(self)


    def Update(self):
        """Update(CFluidDriver self)"""
        return _pysu2ad.CFluidDriver_Update(self)


    def Output(self, InnerIter):
        """Output(CFluidDriver self, unsigned long InnerIter)"""
        return _pysu2ad.CFluidDriver_Output(self, InnerIter)


    def Monitor(self, ExtIter):
        """Monitor(CFluidDriver self, unsigned long ExtIter) -> bool"""
        return _pysu2ad.CFluidDriver_Monitor(self, ExtIter)


    def Preprocess(self, Iter):
        """Preprocess(CFluidDriver self, unsigned long Iter)"""
        return _pysu2ad.CFluidDriver_Preprocess(self, Iter)


    def DynamicMeshUpdate(self, TimeIter):
        """DynamicMeshUpdate(CFluidDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CFluidDriver_DynamicMeshUpdate(self, TimeIter)


    def Transfer_Data(self, donorZone, targetZone):
        """Transfer_Data(CFluidDriver self, unsigned short donorZone, unsigned short targetZone)"""
        return _pysu2ad.CFluidDriver_Transfer_Data(self, donorZone, targetZone)

CFluidDriver_swigregister = _pysu2ad.CFluidDriver_swigregister
CFluidDriver_swigregister(CFluidDriver)

class CTurbomachineryDriver(CFluidDriver):
    """Proxy of C++ CTurbomachineryDriver class."""

    __swig_setmethods__ = {}
    for _s in [CFluidDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CTurbomachineryDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [CFluidDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CTurbomachineryDriver, name)
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        """__init__(CTurbomachineryDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CTurbomachineryDriver"""
        this = _pysu2ad.new_CTurbomachineryDriver(confFile, val_nZone, MPICommunicator)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pysu2ad.delete_CTurbomachineryDriver
    __del__ = lambda self: None

    def Run(self):
        """Run(CTurbomachineryDriver self)"""
        return _pysu2ad.CTurbomachineryDriver_Run(self)


    def SetMixingPlane(self, iZone):
        """SetMixingPlane(CTurbomachineryDriver self, unsigned short iZone)"""
        return _pysu2ad.CTurbomachineryDriver_SetMixingPlane(self, iZone)


    def SetTurboPerformance(self, targetZone):
        """SetTurboPerformance(CTurbomachineryDriver self, unsigned short targetZone)"""
        return _pysu2ad.CTurbomachineryDriver_SetTurboPerformance(self, targetZone)


    def Monitor(self, TimeIter):
        """Monitor(CTurbomachineryDriver self, unsigned long TimeIter) -> bool"""
        return _pysu2ad.CTurbomachineryDriver_Monitor(self, TimeIter)

CTurbomachineryDriver_swigregister = _pysu2ad.CTurbomachineryDriver_swigregister
CTurbomachineryDriver_swigregister(CTurbomachineryDriver)

class CHBDriver(CFluidDriver):
    """Proxy of C++ CHBDriver class."""

    __swig_setmethods__ = {}
    for _s in [CFluidDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CHBDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [CFluidDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CHBDriver, name)
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        """__init__(CHBDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CHBDriver"""
        this = _pysu2ad.new_CHBDriver(confFile, val_nZone, MPICommunicator)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pysu2ad.delete_CHBDriver
    __del__ = lambda self: None

    def Run(self):
        """Run(CHBDriver self)"""
        return _pysu2ad.CHBDriver_Run(self)


    def SetHarmonicBalance(self, iZone):
        """SetHarmonicBalance(CHBDriver self, unsigned short iZone)"""
        return _pysu2ad.CHBDriver_SetHarmonicBalance(self, iZone)


    def StabilizeHarmonicBalance(self):
        """StabilizeHarmonicBalance(CHBDriver self)"""
        return _pysu2ad.CHBDriver_StabilizeHarmonicBalance(self)


    def ComputeHB_Operator(self):
        """ComputeHB_Operator(CHBDriver self)"""
        return _pysu2ad.CHBDriver_ComputeHB_Operator(self)


    def Update(self):
        """Update(CHBDriver self)"""
        return _pysu2ad.CHBDriver_Update(self)


    def ResetConvergence(self):
        """ResetConvergence(CHBDriver self)"""
        return _pysu2ad.CHBDriver_ResetConvergence(self)

CHBDriver_swigregister = _pysu2ad.CHBDriver_swigregister
CHBDriver_swigregister(CHBDriver)

class CSinglezoneDriver(CDriver):
    """Proxy of C++ CSinglezoneDriver class."""

    __swig_setmethods__ = {}
    for _s in [CDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CSinglezoneDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [CDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CSinglezoneDriver, name)
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        """__init__(CSinglezoneDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CSinglezoneDriver"""
        this = _pysu2ad.new_CSinglezoneDriver(confFile, val_nZone, MPICommunicator)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pysu2ad.delete_CSinglezoneDriver
    __del__ = lambda self: None

    def StartSolver(self):
        """StartSolver(CSinglezoneDriver self)"""
        return _pysu2ad.CSinglezoneDriver_StartSolver(self)


    def Preprocess(self, TimeIter):
        """Preprocess(CSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CSinglezoneDriver_Preprocess(self, TimeIter)


    def Run(self):
        """Run(CSinglezoneDriver self)"""
        return _pysu2ad.CSinglezoneDriver_Run(self)


    def Postprocess(self):
        """Postprocess(CSinglezoneDriver self)"""
        return _pysu2ad.CSinglezoneDriver_Postprocess(self)


    def Update(self):
        """Update(CSinglezoneDriver self)"""
        return _pysu2ad.CSinglezoneDriver_Update(self)


    def Output(self, TimeIter):
        """Output(CSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CSinglezoneDriver_Output(self, TimeIter)


    def DynamicMeshUpdate(self, TimeIter):
        """DynamicMeshUpdate(CSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CSinglezoneDriver_DynamicMeshUpdate(self, TimeIter)


    def SetInitialMesh(self):
        """SetInitialMesh(CSinglezoneDriver self)"""
        return _pysu2ad.CSinglezoneDriver_SetInitialMesh(self)


    def Monitor(self, TimeIter):
        """Monitor(CSinglezoneDriver self, unsigned long TimeIter) -> bool"""
        return _pysu2ad.CSinglezoneDriver_Monitor(self, TimeIter)


    def GetTimeConvergence(self):
        """GetTimeConvergence(CSinglezoneDriver self) -> bool"""
        return _pysu2ad.CSinglezoneDriver_GetTimeConvergence(self)


    def Runtime_Options(self):
        """Runtime_Options(CSinglezoneDriver self)"""
        return _pysu2ad.CSinglezoneDriver_Runtime_Options(self)

CSinglezoneDriver_swigregister = _pysu2ad.CSinglezoneDriver_swigregister
CSinglezoneDriver_swigregister(CSinglezoneDriver)

class CMultizoneDriver(CDriver):
    """Proxy of C++ CMultizoneDriver class."""

    __swig_setmethods__ = {}
    for _s in [CDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CMultizoneDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [CDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CMultizoneDriver, name)
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        """__init__(CMultizoneDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CMultizoneDriver"""
        this = _pysu2ad.new_CMultizoneDriver(confFile, val_nZone, MPICommunicator)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pysu2ad.delete_CMultizoneDriver
    __del__ = lambda self: None

    def StartSolver(self):
        """StartSolver(CMultizoneDriver self)"""
        return _pysu2ad.CMultizoneDriver_StartSolver(self)


    def Preprocess(self, TimeIter):
        """Preprocess(CMultizoneDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CMultizoneDriver_Preprocess(self, TimeIter)


    def Corrector(self, val_iZone):
        """Corrector(CMultizoneDriver self, unsigned short val_iZone)"""
        return _pysu2ad.CMultizoneDriver_Corrector(self, val_iZone)


    def Run_GaussSeidel(self):
        """Run_GaussSeidel(CMultizoneDriver self)"""
        return _pysu2ad.CMultizoneDriver_Run_GaussSeidel(self)


    def Run_Jacobi(self):
        """Run_Jacobi(CMultizoneDriver self)"""
        return _pysu2ad.CMultizoneDriver_Run_Jacobi(self)


    def Update(self):
        """Update(CMultizoneDriver self)"""
        return _pysu2ad.CMultizoneDriver_Update(self)


    def Output(self, TimeIter):
        """Output(CMultizoneDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CMultizoneDriver_Output(self, TimeIter)


    def OuterConvergence(self, OuterIter):
        """OuterConvergence(CMultizoneDriver self, unsigned long OuterIter) -> bool"""
        return _pysu2ad.CMultizoneDriver_OuterConvergence(self, OuterIter)


    def DynamicMeshUpdate(self, *args):
        """
        DynamicMeshUpdate(CMultizoneDriver self, unsigned long TimeIter)
        DynamicMeshUpdate(CMultizoneDriver self, unsigned short val_iZone, unsigned long TimeIter)
        """
        return _pysu2ad.CMultizoneDriver_DynamicMeshUpdate(self, *args)


    def Transfer_Data(self, donorZone, targetZone):
        """Transfer_Data(CMultizoneDriver self, unsigned short donorZone, unsigned short targetZone) -> bool"""
        return _pysu2ad.CMultizoneDriver_Transfer_Data(self, donorZone, targetZone)


    def Monitor(self, TimeIter):
        """Monitor(CMultizoneDriver self, unsigned long TimeIter) -> bool"""
        return _pysu2ad.CMultizoneDriver_Monitor(self, TimeIter)


    def GetTimeConvergence(self):
        """GetTimeConvergence(CMultizoneDriver self) -> bool"""
        return _pysu2ad.CMultizoneDriver_GetTimeConvergence(self)

CMultizoneDriver_swigregister = _pysu2ad.CMultizoneDriver_swigregister
CMultizoneDriver_swigregister(CMultizoneDriver)

class CDiscAdjSinglezoneDriver(CSinglezoneDriver):
    """Proxy of C++ CDiscAdjSinglezoneDriver class."""

    __swig_setmethods__ = {}
    for _s in [CSinglezoneDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CDiscAdjSinglezoneDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [CSinglezoneDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CDiscAdjSinglezoneDriver, name)
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        """__init__(CDiscAdjSinglezoneDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CDiscAdjSinglezoneDriver"""
        this = _pysu2ad.new_CDiscAdjSinglezoneDriver(confFile, val_nZone, MPICommunicator)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pysu2ad.delete_CDiscAdjSinglezoneDriver
    __del__ = lambda self: None

    def Preprocess(self, TimeIter):
        """Preprocess(CDiscAdjSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_Preprocess(self, TimeIter)


    def Run(self):
        """Run(CDiscAdjSinglezoneDriver self)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_Run(self)


    def Postprocess(self):
        """Postprocess(CDiscAdjSinglezoneDriver self)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_Postprocess(self)


    def SetRecording(self, kind_recording):
        """SetRecording(CDiscAdjSinglezoneDriver self, unsigned short kind_recording)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_SetRecording(self, kind_recording)


    def DirectRun(self, kind_recording):
        """DirectRun(CDiscAdjSinglezoneDriver self, unsigned short kind_recording)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_DirectRun(self, kind_recording)


    def SetObjFunction(self):
        """SetObjFunction(CDiscAdjSinglezoneDriver self)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_SetObjFunction(self)


    def SetAdj_ObjFunction(self):
        """SetAdj_ObjFunction(CDiscAdjSinglezoneDriver self)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_SetAdj_ObjFunction(self)


    def Print_DirectResidual(self, kind_recording):
        """Print_DirectResidual(CDiscAdjSinglezoneDriver self, unsigned short kind_recording)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_Print_DirectResidual(self, kind_recording)


    def MainRecording(self):
        """MainRecording(CDiscAdjSinglezoneDriver self)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_MainRecording(self)


    def SecondaryRecording(self):
        """SecondaryRecording(CDiscAdjSinglezoneDriver self)"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_SecondaryRecording(self)


    def GetTimeConvergence(self):
        """GetTimeConvergence(CDiscAdjSinglezoneDriver self) -> bool"""
        return _pysu2ad.CDiscAdjSinglezoneDriver_GetTimeConvergence(self)

CDiscAdjSinglezoneDriver_swigregister = _pysu2ad.CDiscAdjSinglezoneDriver_swigregister
CDiscAdjSinglezoneDriver_swigregister(CDiscAdjSinglezoneDriver)

# This file is compatible with both classic and new-style classes.

