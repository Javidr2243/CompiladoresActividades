# Generated from Patito.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PatitoParser import PatitoParser
else:
    from PatitoParser import PatitoParser

# This class defines a complete generic visitor for a parse tree produced by PatitoParser.

class PatitoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PatitoParser#tipo.
    def visitTipo(self, ctx:PatitoParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#cte.
    def visitCte(self, ctx:PatitoParser.CteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#factor.
    def visitFactor(self, ctx:PatitoParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#termino.
    def visitTermino(self, ctx:PatitoParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#exp.
    def visitExp(self, ctx:PatitoParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#expresion.
    def visitExpresion(self, ctx:PatitoParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#asigna.
    def visitAsigna(self, ctx:PatitoParser.AsignaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#llamada.
    def visitLlamada(self, ctx:PatitoParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#imprime.
    def visitImprime(self, ctx:PatitoParser.ImprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#entrada.
    def visitEntrada(self, ctx:PatitoParser.EntradaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#regresa.
    def visitRegresa(self, ctx:PatitoParser.RegresaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#condicion.
    def visitCondicion(self, ctx:PatitoParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#ciclo.
    def visitCiclo(self, ctx:PatitoParser.CicloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#estatuto.
    def visitEstatuto(self, ctx:PatitoParser.EstatutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#cuerpo.
    def visitCuerpo(self, ctx:PatitoParser.CuerpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#vars.
    def visitVars(self, ctx:PatitoParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#funcs.
    def visitFuncs(self, ctx:PatitoParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatitoParser#programa.
    def visitPrograma(self, ctx:PatitoParser.ProgramaContext):
        return self.visitChildren(ctx)



del PatitoParser